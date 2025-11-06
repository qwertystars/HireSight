"""Resume parsing service - HUMAN IMPLEMENTATION REQUIRED.

This service handles PDF and DOCX resume file parsing.
Currently contains stub implementation.
"""
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


def extract_text_from_resume(file_path: str) -> str:
    """
    Extract plain text from PDF or DOCX resume.

    This function must be implemented by a human developer to handle:
    - PDF text extraction (using PyPDF2, pdfplumber, or similar)
    - DOCX text extraction (using python-docx or similar)
    - Text cleaning and normalization

    Args:
        file_path: Path to resume file (e.g., "uploads/resume_123.pdf")

    Returns:
        Extracted text as string

    Raises:
        ValueError: If file format unsupported or parsing fails
        FileNotFoundError: If file doesn't exist

    Example:
        >>> text = extract_text_from_resume("uploads/resume_123.pdf")
        >>> print(text[:100])
        "John Doe\\nSoftware Engineer\\n\\nExperience:\\n- Worked on climate tech projects..."
    """
    logger.warning(f"STUB: extract_text_from_resume called with file_path={file_path}")
    logger.warning("Human implementation required for resume parsing")

    # Stub implementation - returns mock text for testing
    # TODO: Implement actual PDF/DOCX parsing
    return f"""
    MOCK RESUME TEXT - IMPLEMENT PDF/DOCX PARSING

    John Doe
    Software Engineer

    SKILLS:
    Python, JavaScript, React, Machine Learning, Climate Tech

    EXPERIENCE:
    - 3 years building climate data analytics platforms
    - Led sustainability-focused EdTech projects
    - Contributed to open source environmental monitoring tools

    VALUES:
    - Passionate about climate change solutions
    - Committed to making positive social impact
    - Believe in accessible education for all

    File: {file_path}
    """


def validate_resume_file(filename: str, content_type: str) -> bool:
    """
    Validate resume file format.

    Args:
        filename: Name of the uploaded file
        content_type: MIME type of the file

    Returns:
        True if valid, False otherwise

    Example:
        >>> validate_resume_file("resume.pdf", "application/pdf")
        True
        >>> validate_resume_file("resume.txt", "text/plain")
        False
    """
    valid_extensions = [".pdf", ".docx"]
    valid_mime_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    # Check file extension
    has_valid_extension = any(filename.lower().endswith(ext) for ext in valid_extensions)

    # Check MIME type
    has_valid_mime = content_type in valid_mime_types

    return has_valid_extension and has_valid_mime
