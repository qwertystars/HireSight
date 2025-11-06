"""Pydantic schemas for request/response validation."""
from app.schemas.candidate import (
    CandidateCreate,
    CandidateResponse,
    CandidateUploadResponse,
    CandidateBriefResponse
)
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyWithAlignmentResponse,
    CompanyListResponse
)
from app.schemas.alignment import (
    AlignmentRequest,
    AlignmentResult,
    SkillGapRequest,
    SkillGapResponse
)
from app.schemas.interest import (
    InterestCreate,
    InterestResponse,
    InterestDeleteResponse
)
from app.schemas.common import (
    HealthCheckResponse,
    ErrorResponse,
    MessageResponse
)

__all__ = [
    "CandidateCreate",
    "CandidateResponse",
    "CandidateUploadResponse",
    "CandidateBriefResponse",
    "CompanyCreate",
    "CompanyResponse",
    "CompanyWithAlignmentResponse",
    "CompanyListResponse",
    "AlignmentRequest",
    "AlignmentResult",
    "SkillGapRequest",
    "SkillGapResponse",
    "InterestCreate",
    "InterestResponse",
    "InterestDeleteResponse",
    "HealthCheckResponse",
    "ErrorResponse",
    "MessageResponse",
]
