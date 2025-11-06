"""Interest tracking database model."""
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Interest(Base):
    """Interest tracking model for candidate-company relationships."""

    __tablename__ = "interests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Reference to candidate"
    )
    company_id = Column(
        Integer,
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Reference to company"
    )
    tracked_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    # Add composite unique constraint to prevent duplicates
    # Add composite indexes for common queries
    __table_args__ = (
        UniqueConstraint('candidate_id', 'company_id', name='uq_candidate_company'),
        Index('idx_interest_candidate', 'candidate_id'),
        Index('idx_interest_company', 'company_id'),
        Index('idx_interest_tracked_at', 'tracked_at'),
        Index('idx_interest_composite', 'candidate_id', 'company_id'),
    )

    def __repr__(self) -> str:
        """String representation of Interest."""
        return f"<Interest(id={self.id}, candidate_id={self.candidate_id}, company_id={self.company_id})>"
