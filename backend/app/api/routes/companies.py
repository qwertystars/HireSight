"""Company-related endpoints."""
import logging
import json
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.candidate import Candidate
from app.models.company import Company
from app.schemas.company import CompanyWithAlignmentResponse
from app.services.alignment_service import batch_calculate_alignment

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["companies"])


@router.get(
    "/companies",
    response_model=List[CompanyWithAlignmentResponse],
    status_code=status.HTTP_200_OK,
    summary="Get ranked companies",
    description="Get all companies ranked by alignment score for a specific candidate"
)
async def get_ranked_companies(
    candidate_id: int = Query(..., gt=0, description="Candidate ID"),
    threshold: Optional[float] = Query(None, ge=0, le=100, description="Minimum alignment threshold"),
    db: Session = Depends(get_db)
) -> List[CompanyWithAlignmentResponse]:
    """
    Get companies ranked by alignment score for a candidate.

    Args:
        candidate_id: ID of the candidate
        threshold: Optional minimum alignment score threshold (0-100)
        db: Database session

    Returns:
        List of companies with alignment scores, sorted by score (highest first)

    Raises:
        HTTPException 404: Candidate not found
        HTTPException 500: Processing failed
    """
    logger.info(f"Fetching ranked companies for candidate {candidate_id}")

    # Check if candidate exists
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not candidate:
        logger.warning(f"Candidate not found: {candidate_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Candidate with id {candidate_id} not found"
        )

    try:
        # Calculate alignment scores for all companies
        alignment_scores = batch_calculate_alignment(candidate_id, db)

        # Get all companies
        companies = db.query(Company).all()

        # Build response
        results = []
        for company in companies:
            alignment_data = alignment_scores.get(company.id, {"score": 0.0, "reasoning": "No data"})
            score = alignment_data["score"]

            # Apply threshold filter if specified
            if threshold is not None and score < threshold:
                continue

            results.append(
                CompanyWithAlignmentResponse(
                    id=company.id,
                    name=company.name,
                    alignment_percentage=score,
                    reasoning=alignment_data["reasoning"]
                )
            )

        # Sort by alignment score (descending)
        results.sort(key=lambda x: x.alignment_percentage, reverse=True)

        logger.info(f"Returning {len(results)} companies for candidate {candidate_id}")
        return results

    except Exception as e:
        logger.error(f"Failed to calculate alignments: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to calculate alignment scores: {str(e)}"
        )
