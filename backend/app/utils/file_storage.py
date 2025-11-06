"""File storage utilities."""
import os
import uuid
import shutil
import logging
from pathlib import Path
from typing import Tuple
from fastapi import UploadFile

from app.core.config import settings

logger = logging.getLogger(__name__)


async def save_uploaded_file(file: UploadFile) -> Tuple[str, str]:
    """
    Save an uploaded file to the uploads directory with a unique filename.

    Args:
        file: FastAPI UploadFile object

    Returns:
        Tuple of (relative_path, absolute_path)

    Raises:
        IOError: If file cannot be saved

    Example:
        >>> file = UploadFile(...)
        >>> rel_path, abs_path = await save_uploaded_file(file)
        >>> print(rel_path)
        "uploads/resume_a1b2c3d4_20231024.pdf"
    """
    try:
        # Ensure upload directory exists
        upload_dir = Path(settings.upload_dir)
        upload_dir.mkdir(parents=True, exist_ok=True)

        # Generate unique filename
        file_extension = Path(file.filename).suffix
        unique_filename = f"resume_{uuid.uuid4().hex[:8]}_{file.filename}"
        file_path = upload_dir / unique_filename

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        relative_path = str(file_path.relative_to(Path.cwd()))
        absolute_path = str(file_path.absolute())

        logger.info(f"File saved: {relative_path} ({file.size} bytes)")

        return relative_path, absolute_path

    except Exception as e:
        logger.error(f"Failed to save file {file.filename}: {e}")
        raise IOError(f"Failed to save file: {e}")


def delete_file(file_path: str) -> bool:
    """
    Delete a file from the filesystem.

    Args:
        file_path: Path to file (relative or absolute)

    Returns:
        True if deleted successfully, False otherwise

    Example:
        >>> delete_file("uploads/resume_12345.pdf")
        True
    """
    try:
        path = Path(file_path)
        if path.exists() and path.is_file():
            path.unlink()
            logger.info(f"File deleted: {file_path}")
            return True
        else:
            logger.warning(f"File not found: {file_path}")
            return False
    except Exception as e:
        logger.error(f"Failed to delete file {file_path}: {e}")
        return False


def get_file_size(file_path: str) -> int:
    """
    Get file size in bytes.

    Args:
        file_path: Path to file

    Returns:
        File size in bytes, or 0 if file doesn't exist

    Example:
        >>> size = get_file_size("uploads/resume.pdf")
        >>> print(f"{size / 1024 / 1024:.2f} MB")
        "2.45 MB"
    """
    try:
        return Path(file_path).stat().st_size
    except Exception:
        return 0


def validate_file_size(file: UploadFile) -> bool:
    """
    Validate that file size is within limits.

    Args:
        file: FastAPI UploadFile object

    Returns:
        True if valid, False otherwise

    Example:
        >>> if not validate_file_size(file):
        ...     raise HTTPException(400, "File too large")
    """
    if file.size is None:
        return True  # Size unknown, allow upload (will check during save)

    return file.size <= settings.max_upload_size
