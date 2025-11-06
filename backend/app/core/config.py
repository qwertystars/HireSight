"""Application configuration using Pydantic Settings."""
import os
from typing import List
from functools import lru_cache
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Application
    app_name: str = "HireSight"
    app_version: str = "1.0.0"
    debug: bool = Field(default=False, description="Debug mode")

    # Database
    database_url: str = Field(
        default="sqlite:///./data/hiresight.db",
        description="Database connection URL"
    )

    # File Storage
    upload_dir: str = Field(default="./uploads", description="Upload directory path")
    max_upload_size: int = Field(default=10_000_000, description="Max upload size in bytes (10MB)")
    allowed_extensions: List[str] = Field(
        default=[".pdf", ".docx"],
        description="Allowed file extensions"
    )

    # CORS
    cors_origins: str = Field(
        default="http://localhost:5173,http://localhost:3000",
        description="Comma-separated CORS origins"
    )

    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(default="json", description="Log format: json or text")

    # Performance
    enable_caching: bool = Field(default=True, description="Enable response caching")
    cache_ttl: int = Field(default=300, description="Cache TTL in seconds")

    # Production Settings
    environment: str = Field(default="development", description="Environment: development, staging, production")

    # Render.com specific
    port: int = Field(default=8000, description="Server port")
    host: str = Field(default="0.0.0.0", description="Server host")
    workers: int = Field(default=1, description="Number of worker processes")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    @field_validator("cors_origins")
    @classmethod
    def parse_cors_origins(cls, v: str) -> List[str]:
        """Parse comma-separated CORS origins."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        v = v.upper()
        if v not in valid_levels:
            raise ValueError(f"Invalid log level. Must be one of {valid_levels}")
        return v

    @field_validator("upload_dir")
    @classmethod
    def create_upload_dir(cls, v: str) -> str:
        """Ensure upload directory exists."""
        os.makedirs(v, exist_ok=True)
        return v

    @property
    def is_production(self) -> bool:
        """Check if running in production."""
        return self.environment.lower() == "production"

    @property
    def is_development(self) -> bool:
        """Check if running in development."""
        return self.environment.lower() == "development"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Global settings instance
settings = get_settings()
