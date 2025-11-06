"""Candidate schemas for request/response validation."""
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional


class CandidateBase(BaseModel):
    """Base candidate schema."""

    pass


class CandidateCreate(CandidateBase):
    """Schema for creating a candidate (via resume upload)."""

    pass  # File upload handled separately


class CandidateResponse(BaseModel):
    """Schema for candidate response."""

    id: int = Field(..., description="Candidate ID")
    resume_path: str = Field(..., description="Path to resume file")
    extracted_skills: Optional[List[str]] = Field(None, description="Extracted skills")
    extracted_domains: Optional[List[str]] = Field(None, description="Extracted domains")
    values_signals: Optional[List[str]] = Field(None, description="Values signals")
    created_at: datetime = Field(..., description="Creation timestamp")

    model_config = ConfigDict(from_attributes=True)


class CandidateUploadResponse(BaseModel):
    """Schema for resume upload response."""

    candidate_id: int = Field(..., description="Created candidate ID")
    message: str = Field(..., description="Success message")


class CandidateBriefResponse(BaseModel):
    """Brief candidate information for listing."""

    candidate_id: int = Field(..., description="Candidate ID")
    name: str = Field(default="Candidate", description="Candidate name (if extracted)")
    alignment_percentage: float = Field(..., description="Alignment score percentage")
    reasoning: str = Field(..., description="Reasoning for alignment score")
