"""Interest tracking schemas for request/response validation."""
from pydantic import BaseModel, Field
from datetime import datetime


class InterestCreate(BaseModel):
    """Schema for creating an interest record."""

    candidate_id: int = Field(..., gt=0, description="Candidate ID")
    company_id: int = Field(..., gt=0, description="Company ID")


class InterestResponse(BaseModel):
    """Schema for interest tracking response."""

    message: str = Field(..., description="Success message")
    company_name: str = Field(..., description="Company name")
    tracked_at: datetime = Field(..., description="Timestamp when interest was tracked")


class InterestDeleteResponse(BaseModel):
    """Schema for interest deletion response."""

    message: str = Field(..., description="Success message")
