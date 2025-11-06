"""NLP service for extracting skills, domains, and values - HUMAN IMPLEMENTATION REQUIRED.

This service handles natural language processing of resume text.
Currently contains stub implementation with mock data.
"""
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


def extract_skills_and_domains(text: str) -> Dict[str, List[str]]:
    """
    Extract structured data from resume text using NLP/ML.

    This function must be implemented by a human developer to handle:
    - Skills extraction (technical keywords, frameworks, tools)
    - Domain identification (industry sectors like "climate tech", "EdTech")
    - Values signals detection (passion indicators like "mission-driven", "impact")

    Implementation suggestions:
    - Use spaCy for NER and keyword extraction
    - Use keyword matching with predefined skill taxonomies
    - Implement sentiment analysis for values signals
    - Use TF-IDF or word embeddings for domain classification

    Args:
        text: Resume text content

    Returns:
        Dictionary with keys:
            - "skills": List of technical skills (e.g., ["Python", "React", "ML"])
            - "domains": List of industry domains (e.g., ["climate tech", "education"])
            - "values_signals": List of passion/values indicators

    Example:
        >>> text = "Passionate about climate change. 5 years Python experience..."
        >>> result = extract_skills_and_domains(text)
        >>> print(result)
        {
            "skills": ["Python", "JavaScript", "Machine Learning"],
            "domains": ["climate tech", "sustainability"],
            "values_signals": ["climate change", "passion", "impact"]
        }
    """
    logger.warning("STUB: extract_skills_and_domains called")
    logger.warning("Human implementation required for NLP extraction")

    # Stub implementation - returns mock data for testing
    # TODO: Implement actual NLP/ML-based extraction
    mock_skills = []
    mock_domains = []
    mock_values = []

    # Simple keyword matching for demo purposes
    text_lower = text.lower()

    # Skills detection (basic)
    skill_keywords = {
        "python": "Python",
        "javascript": "JavaScript",
        "react": "React",
        "machine learning": "Machine Learning",
        "ml": "Machine Learning",
        "aws": "AWS",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "fastapi": "FastAPI",
        "sql": "SQL",
        "data": "Data Analysis"
    }

    for keyword, skill in skill_keywords.items():
        if keyword in text_lower and skill not in mock_skills:
            mock_skills.append(skill)

    # Domain detection (basic)
    domain_keywords = {
        "climate": "climate tech",
        "sustainability": "climate tech",
        "environment": "climate tech",
        "education": "EdTech",
        "edtech": "EdTech",
        "teaching": "EdTech",
        "health": "HealthTech",
        "medical": "HealthTech",
        "healthcare": "HealthTech"
    }

    for keyword, domain in domain_keywords.items():
        if keyword in text_lower and domain not in mock_domains:
            mock_domains.append(domain)

    # Values signals detection (basic)
    values_keywords = {
        "passion": "passionate",
        "impact": "social impact",
        "mission": "mission-driven",
        "sustainability": "sustainability",
        "accessible": "accessibility",
        "inclusive": "inclusivity",
        "community": "community focus"
    }

    for keyword, value in values_keywords.items():
        if keyword in text_lower and value not in mock_values:
            mock_values.append(value)

    # Ensure we have at least some data for demo
    if not mock_skills:
        mock_skills = ["Python", "JavaScript"]
    if not mock_domains:
        mock_domains = ["technology"]
    if not mock_values:
        mock_values = ["professional growth"]

    return {
        "skills": mock_skills,
        "domains": mock_domains,
        "values_signals": mock_values
    }
