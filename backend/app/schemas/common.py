"""Common schemas used across the application."""
from pydantic import BaseModel, Field
from typing import Optional, Any, Dict


class HealthCheckResponse(BaseModel):
    """Schema for health check response."""

    status: str = Field(..., description="Service status")
    version: str = Field(..., description="Application version")
    database: str = Field(..., description="Database connection status")


class ErrorResponse(BaseModel):
    """Schema for error responses."""

    detail: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code")


class MessageResponse(BaseModel):
    """Schema for simple message responses."""

    message: str = Field(..., description="Response message")
    data: Optional[Dict[str, Any]] = Field(None, description="Additional data")
