"""Alignment and skill gap analysis endpoints."""
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.candidate import Candidate
from app.models.company import Company
from app.schemas.alignment import SkillGapRequest, SkillGapResponse
from app.services.skill_gap_service import calculate_skill_gap
from app.services.alignment_service import calculate_alignment

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["alignment"])


@router.post(
    "/check-gap",
    response_model=SkillGapResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze skill gap",
    description="Analyze skill gaps between a candidate and a company"
)
async def check_skill_gap(
    request: SkillGapRequest,
    db: Session = Depends(get_db)
) -> SkillGapResponse:
    """
    Analyze skill gap between candidate and company.

    Args:
        request: SkillGapRequest with candidate_id and company_id
        db: Database session

    Returns:
        SkillGapResponse with missing skills and learning recommendations

    Raises:
        HTTPException 404: Candidate or company not found
        HTTPException 500: Processing failed
    """
    logger.info(f"Analyzing skill gap: candidate={request.candidate_id}, company={request.company_id}")

    # Verify candidate exists
    candidate = db.query(Candidate).filter(Candidate.id == request.candidate_id).first()
    if not candidate:
        logger.warning(f"Candidate not found: {request.candidate_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Candidate with id {request.candidate_id} not found"
        )

    # Verify company exists
    company = db.query(Company).filter(Company.id == request.company_id).first()
    if not company:
        logger.warning(f"Company not found: {request.company_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {request.company_id} not found"
        )

    try:
        # Calculate skill gap
        gap_analysis = calculate_skill_gap(request.candidate_id, request.company_id, db)

        # Calculate current alignment
        alignment = calculate_alignment(request.candidate_id, request.company_id, db)

        logger.info(f"Skill gap analyzed: {len(gap_analysis['missing_skills'])} skills missing")

        return SkillGapResponse(
            company_name=company.name,
            current_alignment=alignment["score"],
            missing_skills=gap_analysis["missing_skills"],
            recommended_learning_path=gap_analysis["recommended_learning_path"]
        )

    except ValueError as e:
        logger.error(f"Skill gap analysis failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error during skill gap analysis: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to analyze skill gap: {str(e)}"
        )
