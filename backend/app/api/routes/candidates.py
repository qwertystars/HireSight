"""Candidate-related endpoints."""
import logging
import json
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.config import settings
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateUploadResponse
from app.services.resume_parser import extract_text_from_resume, validate_resume_file
from app.services.nlp_service import extract_skills_and_domains
from app.utils.file_storage import save_uploaded_file, validate_file_size

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["candidates"])


@router.post(
    "/upload-resume",
    response_model=CandidateUploadResponse,
    status_code=status.HTTP_200_OK,
    summary="Upload candidate resume",
    description="Upload and process a candidate's resume (PDF or DOCX)"
)
async def upload_resume(
    file: UploadFile = File(..., description="Resume file (PDF or DOCX)"),
    db: Session = Depends(get_db)
) -> CandidateUploadResponse:
    """
    Upload and process candidate resume.

    Steps:
    1. Validate file format and size
    2. Save file to uploads directory
    3. Extract text from resume
    4. Extract skills, domains, and values using NLP
    5. Create candidate record in database

    Args:
        file: Uploaded resume file
        db: Database session

    Returns:
        CandidateUploadResponse with candidate_id and success message

    Raises:
        HTTPException 400: Invalid file format or size
        HTTPException 500: Processing failed
    """
    logger.info(f"Processing resume upload: {file.filename}")

    # Validate file format
    if not validate_resume_file(file.filename, file.content_type):
        logger.warning(f"Invalid file format: {file.filename} ({file.content_type})")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format. Only PDF and DOCX files are allowed."
        )

    # Validate file size
    if not validate_file_size(file):
        logger.warning(f"File too large: {file.filename} ({file.size} bytes)")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large. Maximum size is {settings.max_upload_size / 1024 / 1024:.1f}MB."
        )

    try:
        # Save uploaded file
        relative_path, absolute_path = await save_uploaded_file(file)

        # Extract text from resume
        extracted_text = extract_text_from_resume(absolute_path)

        # Extract structured data using NLP
        nlp_data = extract_skills_and_domains(extracted_text)

        # Create candidate record
        candidate = Candidate(
            resume_path=relative_path,
            extracted_text=extracted_text,
            extracted_skills=json.dumps(nlp_data.get("skills", [])),
            extracted_domains=json.dumps(nlp_data.get("domains", [])),
            values_signals=json.dumps(nlp_data.get("values_signals", []))
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        logger.info(f"Resume processed successfully: candidate_id={candidate.id}")

        return CandidateUploadResponse(
            candidate_id=candidate.id,
            message="Resume processed successfully"
        )

    except Exception as e:
        logger.error(f"Failed to process resume: {e}", exc_info=True)
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process resume: {str(e)}"
        )
