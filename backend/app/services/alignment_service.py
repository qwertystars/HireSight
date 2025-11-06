"""Alignment calculation service - HUMAN IMPLEMENTATION REQUIRED.

This service calculates alignment scores between candidates and companies.
Currently contains stub implementation with basic matching logic.
"""
import logging
import json
from typing import Dict
from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.models.company import Company

logger = logging.getLogger(__name__)


def calculate_alignment(candidate_id: int, company_id: int, db: Session) -> Dict[str, any]:
    """
    Calculate alignment score using weighted algorithm: 60% domain + 40% values.

    This function must be implemented by a human developer to provide:
    - Sophisticated domain matching (using NLP, embeddings, or keyword overlap)
    - Values alignment scoring (comparing candidate passion signals with company values)
    - Clear reasoning generation explaining the score
    - Edge case handling (missing data, no overlap, etc.)

    Implementation suggestions:
    - Use cosine similarity for semantic matching
    - Weight recent experience more heavily
    - Detect "passion signals" (years worked, projects built, contributions)
    - Generate human-readable explanations

    Args:
        candidate_id: Candidate database ID
        company_id: Company database ID
        db: SQLAlchemy session

    Returns:
        Dictionary with:
            - "score": float (0-100) representing alignment percentage
            - "reasoning": string explaining why the score was calculated

    Raises:
        ValueError: If candidate or company not found

    Example:
        >>> score = calculate_alignment(1, 5, db)
        >>> print(score)
        {
            "score": 92.5,
            "reasoning": "Strong match: 2 years climate data projects, sustainability values align"
        }
    """
    logger.info(f"Calculating alignment for candidate {candidate_id} and company {company_id}")

    # Fetch candidate and company
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    company = db.query(Company).filter(Company.id == company_id).first()

    if not candidate:
        raise ValueError(f"Candidate with id {candidate_id} not found")
    if not company:
        raise ValueError(f"Company with id {company_id} not found")

    # Parse JSON fields
    try:
        candidate_skills = set(json.loads(candidate.extracted_skills or "[]"))
        candidate_domains = set(json.loads(candidate.extracted_domains or "[]"))
        candidate_values = set(json.loads(candidate.values_signals or "[]"))

        company_skills = set(json.loads(company.required_skills))
        company_values = set(json.loads(company.values))
        company_domain = company.domain.lower()
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return {
            "score": 0.0,
            "reasoning": "Unable to parse candidate or company data"
        }

    # STUB IMPLEMENTATION - Basic matching logic
    # TODO: Implement sophisticated alignment algorithm with NLP/embeddings

    # Domain matching (60% weight)
    domain_score = 0.0
    domain_matches = []

    for c_domain in candidate_domains:
        if c_domain.lower() == company_domain or company_domain in c_domain.lower():
            domain_score = 90.0
            domain_matches.append(c_domain)
        elif any(keyword in c_domain.lower() for keyword in company_domain.split()):
            domain_score = max(domain_score, 70.0)
            domain_matches.append(c_domain)

    # If no exact match, check for related keywords
    if domain_score == 0.0:
        # Default moderate score if candidate has any domain experience
        if candidate_domains:
            domain_score = 40.0

    # Values matching (40% weight)
    values_score = 0.0
    values_matches = []

    # Check for value overlaps
    for c_value in candidate_values:
        for comp_value in company_values:
            if c_value.lower() in comp_value.lower() or comp_value.lower() in c_value.lower():
                values_score += 20.0
                values_matches.append(c_value)
                break

    # Cap values score at 100
    values_score = min(values_score, 100.0)

    # If no values match but candidate has values signals
    if values_score == 0.0 and candidate_values:
        values_score = 30.0  # Give some credit for having values

    # Calculate weighted final score
    final_score = (domain_score * 0.6) + (values_score * 0.4)
    final_score = round(final_score, 1)

    # Generate reasoning
    reasoning_parts = []

    if domain_matches:
        reasoning_parts.append(f"Domain alignment: {', '.join(domain_matches)}")
    else:
        reasoning_parts.append("Limited domain experience match")

    if values_matches:
        reasoning_parts.append(f"Values alignment: {', '.join(values_matches)}")
    else:
        reasoning_parts.append("Some values compatibility")

    # Check skills overlap
    skills_overlap = candidate_skills & company_skills
    if skills_overlap:
        reasoning_parts.append(f"Matching skills: {', '.join(list(skills_overlap)[:3])}")

    reasoning = ". ".join(reasoning_parts)

    logger.info(f"Alignment calculated: score={final_score}, candidate={candidate_id}, company={company_id}")

    return {
        "score": final_score,
        "reasoning": reasoning
    }


def batch_calculate_alignment(candidate_id: int, db: Session) -> Dict[int, Dict[str, any]]:
    """
    Calculate alignment scores for a candidate against all companies.

    Args:
        candidate_id: Candidate database ID
        db: SQLAlchemy session

    Returns:
        Dictionary mapping company_id to alignment result

    Example:
        >>> scores = batch_calculate_alignment(1, db)
        >>> print(scores[5])
        {"score": 92.5, "reasoning": "Strong match..."}
    """
    companies = db.query(Company).all()
    results = {}

    for company in companies:
        try:
            results[company.id] = calculate_alignment(candidate_id, company.id, db)
        except ValueError as e:
            logger.warning(f"Failed to calculate alignment for company {company.id}: {e}")
            results[company.id] = {
                "score": 0.0,
                "reasoning": "Unable to calculate alignment"
            }

    return results
