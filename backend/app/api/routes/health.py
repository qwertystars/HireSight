"""Health check endpoints."""
import logging
from fastapi import APIRouter, status
from app.core.config import settings
from app.core.database import check_db_connection
from app.schemas.common import HealthCheckResponse

logger = logging.getLogger(__name__)

router = APIRouter(tags=["health"])


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check",
    description="Check if the API is running and database is accessible"
)
async def health_check() -> HealthCheckResponse:
    """
    Perform health check on the API and its dependencies.

    Returns:
        HealthCheckResponse with status, version, and database connection status
    """
    # Check database connection
    db_status = "connected" if check_db_connection() else "disconnected"

    if db_status == "disconnected":
        logger.error("Health check failed: database disconnected")

    return HealthCheckResponse(
        status="ok" if db_status == "connected" else "degraded",
        version=settings.app_version,
        database=db_status
    )
