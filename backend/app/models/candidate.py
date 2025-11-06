"""Candidate database model."""
from sqlalchemy import Column, Integer, String, Text, DateTime, Index
from datetime import datetime
from app.core.database import Base


class Candidate(Base):
    """Candidate model for storing resume data and extracted information."""

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resume_path = Column(String(500), nullable=False, comment="Path to stored resume file")
    extracted_text = Column(Text, nullable=True, comment="Full text extracted from resume")
    extracted_skills = Column(Text, nullable=True, comment="JSON array of extracted skills")
    extracted_domains = Column(Text, nullable=True, comment="JSON array of domain keywords")
    values_signals = Column(Text, nullable=True, comment="JSON array of values signals")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    # Add composite index for common queries
    __table_args__ = (
        Index('idx_candidate_created', 'created_at'),
    )

    def __repr__(self) -> str:
        """String representation of Candidate."""
        return f"<Candidate(id={self.id}, created_at={self.created_at})>"
