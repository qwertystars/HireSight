"""Alignment schemas for request/response validation."""
from pydantic import BaseModel, Field
from typing import List


class AlignmentRequest(BaseModel):
    """Schema for alignment calculation request."""

    candidate_id: int = Field(..., gt=0, description="Candidate ID")
    company_id: int = Field(..., gt=0, description="Company ID")


class AlignmentResult(BaseModel):
    """Schema for alignment calculation result."""

    score: float = Field(..., ge=0, le=100, description="Alignment score (0-100)")
    reasoning: str = Field(..., description="Explanation of alignment score")


class SkillGapRequest(BaseModel):
    """Schema for skill gap analysis request."""

    candidate_id: int = Field(..., gt=0, description="Candidate ID")
    company_id: int = Field(..., gt=0, description="Company ID")


class SkillGapResponse(BaseModel):
    """Schema for skill gap analysis response."""

    company_name: str = Field(..., description="Company name")
    current_alignment: float = Field(..., ge=0, le=100, description="Current alignment score")
    missing_skills: List[str] = Field(..., description="Skills the candidate is missing")
    recommended_learning_path: List[str] = Field(..., description="Recommended learning resources")
