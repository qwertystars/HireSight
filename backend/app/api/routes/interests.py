"""Interest tracking endpoints."""
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.database import get_db
from app.models.candidate import Candidate
from app.models.company import Company
from app.models.interest import Interest
from app.schemas.interest import InterestCreate, InterestResponse, InterestDeleteResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["interests"])


@router.post(
    "/track-interest",
    response_model=InterestResponse,
    status_code=status.HTTP_200_OK,
    summary="Track candidate interest",
    description="Record a candidate's interest in a company"
)
async def track_interest(
    request: InterestCreate,
    db: Session = Depends(get_db)
) -> InterestResponse:
    """
    Track candidate interest in a company.

    Args:
        request: InterestCreate with candidate_id and company_id
        db: Database session

    Returns:
        InterestResponse with success message and company name

    Raises:
        HTTPException 400: Interest already tracked
        HTTPException 404: Candidate or company not found
        HTTPException 500: Processing failed
    """
    logger.info(f"Tracking interest: candidate={request.candidate_id}, company={request.company_id}")

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
        # Create interest record
        interest = Interest(
            candidate_id=request.candidate_id,
            company_id=request.company_id
        )

        db.add(interest)
        db.commit()
        db.refresh(interest)

        logger.info(f"Interest tracked: interest_id={interest.id}")

        return InterestResponse(
            message="Interest tracked successfully",
            company_name=company.name,
            tracked_at=interest.tracked_at
        )

    except IntegrityError:
        db.rollback()
        logger.warning(f"Interest already tracked: candidate={request.candidate_id}, company={request.company_id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Interest already tracked for this candidate and company"
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to track interest: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to track interest: {str(e)}"
        )


@router.delete(
    "/track-interest",
    response_model=InterestDeleteResponse,
    status_code=status.HTTP_200_OK,
    summary="Untrack candidate interest",
    description="Remove a candidate's interest record for a company"
)
async def untrack_interest(
    request: InterestCreate,
    db: Session = Depends(get_db)
) -> InterestDeleteResponse:
    """
    Remove candidate interest in a company.

    Args:
        request: InterestCreate with candidate_id and company_id
        db: Database session

    Returns:
        InterestDeleteResponse with success message

    Raises:
        HTTPException 404: Interest record not found
        HTTPException 500: Processing failed
    """
    logger.info(f"Untracking interest: candidate={request.candidate_id}, company={request.company_id}")

    try:
        # Find interest record
        interest = db.query(Interest).filter(
            Interest.candidate_id == request.candidate_id,
            Interest.company_id == request.company_id
        ).first()

        if not interest:
            logger.warning(f"Interest not found: candidate={request.candidate_id}, company={request.company_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interest record not found"
            )

        # Delete interest record
        db.delete(interest)
        db.commit()

        logger.info(f"Interest untracked: interest_id={interest.id}")

        return InterestDeleteResponse(
            message="Interest untracked successfully"
        )

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to untrack interest: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to untrack interest: {str(e)}"
        )
