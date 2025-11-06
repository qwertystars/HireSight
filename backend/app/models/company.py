"""Company database model."""
from sqlalchemy import Column, Integer, String, Text, DateTime, Index
from datetime import datetime
from app.core.database import Base


class Company(Base):
    """Company model for storing company information and requirements."""

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), nullable=False, unique=True, index=True, comment="Company name")
    mission = Column(Text, nullable=False, comment="Mission statement")
    values = Column(Text, nullable=False, comment="JSON array of company values")
    required_skills = Column(Text, nullable=False, comment="JSON array of required skills")
    domain = Column(String(100), nullable=False, index=True, comment="Company domain/industry")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Add indexes for common queries
    __table_args__ = (
        Index('idx_company_domain', 'domain'),
        Index('idx_company_name', 'name'),
    )

    def __repr__(self) -> str:
        """String representation of Company."""
        return f"<Company(id={self.id}, name={self.name}, domain={self.domain})>"
