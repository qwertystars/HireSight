"""Skill gap analysis service."""
import logging
import json
from typing import Dict, List
from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.models.company import Company

logger = logging.getLogger(__name__)


def calculate_skill_gap(candidate_id: int, company_id: int, db: Session) -> Dict[str, any]:
    """
    Calculate skill gap between candidate and company requirements.

    Args:
        candidate_id: Candidate database ID
        company_id: Company database ID
        db: Database session

    Returns:
        Dictionary with:
            - "missing_skills": List of skills candidate needs
            - "recommended_learning_path": List of learning recommendations

    Raises:
        ValueError: If candidate or company not found

    Example:
        >>> gap = calculate_skill_gap(1, 5, db)
        >>> print(gap)
        {
            "missing_skills": ["Kubernetes", "Climate modeling"],
            "recommended_learning_path": ["Kubernetes fundamentals course", ...]
        }
    """
    logger.info(f"Calculating skill gap for candidate {candidate_id} and company {company_id}")

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
        company_skills = set(json.loads(company.required_skills))
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return {
            "missing_skills": [],
            "recommended_learning_path": []
        }

    # Calculate missing skills
    missing_skills = list(company_skills - candidate_skills)

    # Generate learning recommendations
    learning_path = generate_learning_path(missing_skills, company.domain)

    logger.info(f"Skill gap calculated: {len(missing_skills)} skills missing")

    return {
        "missing_skills": missing_skills,
        "recommended_learning_path": learning_path
    }


def generate_learning_path(missing_skills: List[str], domain: str) -> List[str]:
    """
    Generate personalized learning recommendations based on missing skills and domain.

    Args:
        missing_skills: List of skills the candidate needs to learn
        domain: Company domain for context-specific recommendations

    Returns:
        List of learning resource recommendations

    Example:
        >>> path = generate_learning_path(["Python", "ML"], "climate tech")
        >>> print(path)
        ["Python fundamentals for climate data analysis", "Machine Learning for environmental monitoring"]
    """
    if not missing_skills:
        return ["No skill gaps identified! You're well-aligned with this role."]

    learning_recommendations = []

    # Skill-specific resources
    skill_resources = {
        "Python": "Python fundamentals course (Coursera/Udemy)",
        "JavaScript": "Modern JavaScript ES6+ (freeCodeCamp)",
        "React": "React Complete Guide (Official Tutorial)",
        "Machine Learning": "Machine Learning specialization (Andrew Ng)",
        "AWS": "AWS Certified Solutions Architect prep course",
        "Docker": "Docker Mastery course (Udemy)",
        "Kubernetes": "Kubernetes for Beginners (KodeKloud)",
        "SQL": "SQL fundamentals (W3Schools/LeetCode)",
        "Data Analysis": "Data Analysis with Python (DataCamp)",
        "Climate modeling": "Climate Science basics (edX)",
        "Healthcare systems": "Healthcare IT fundamentals",
        "EdTech platforms": "Educational technology frameworks"
    }

    # Add skill-specific recommendations
    for skill in missing_skills[:5]:  # Limit to top 5 for readability
        if skill in skill_resources:
            learning_recommendations.append(skill_resources[skill])
        else:
            learning_recommendations.append(f"{skill} fundamentals course")

    # Add domain-specific recommendation
    domain_resources = {
        "climate tech": "Climate Science basics and environmental data analysis",
        "edtech": "Educational psychology and learning platforms design",
        "healthtech": "Healthcare systems and medical informatics",
        "health tech": "Healthcare systems and medical informatics",
        "social impact": "Social entrepreneurship and impact measurement"
    }

    domain_lower = domain.lower()
    for key, resource in domain_resources.items():
        if key in domain_lower:
            learning_recommendations.append(resource)
            break

    return learning_recommendations
