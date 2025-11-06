"""Company schemas for request/response validation."""
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional


class CompanyBase(BaseModel):
    """Base company schema."""

    name: str = Field(..., min_length=1, max_length=200, description="Company name")
    mission: str = Field(..., min_length=1, description="Mission statement")
    values: List[str] = Field(..., min_items=1, description="Company values")
    required_skills: List[str] = Field(..., min_items=1, description="Required skills")
    domain: str = Field(..., min_length=1, max_length=100, description="Company domain")


class CompanyCreate(CompanyBase):
    """Schema for creating a company."""

    pass


class CompanyResponse(CompanyBase):
    """Schema for company response."""

    id: int = Field(..., description="Company ID")
    created_at: datetime = Field(..., description="Creation timestamp")

    model_config = ConfigDict(from_attributes=True)


class CompanyWithAlignmentResponse(BaseModel):
    """Schema for company with alignment score."""

    id: int = Field(..., description="Company ID")
    name: str = Field(..., description="Company name")
    alignment_percentage: float = Field(..., ge=0, le=100, description="Alignment score (0-100)")
    reasoning: str = Field(..., description="Reasoning for alignment score")


class CompanyListResponse(BaseModel):
    """Schema for company list response."""

    companies: List[CompanyWithAlignmentResponse] = Field(..., description="List of companies with alignment scores")
    total: int = Field(..., description="Total number of companies")
