"""Database models for storing analysis history."""

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import config

Base = declarative_base()


class Analysis(Base):
    """Model for storing business analysis results."""
    
    __tablename__ = "analyses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.now, nullable=False)
    business_name = Column(String(255), nullable=False)
    idea_description = Column(Text, nullable=False)
    target_market = Column(String(500))
    revenue_model = Column(String(500))
    assumptions = Column(Text)
    competitive_landscape = Column(Text)
    
    # Analysis results
    verdict = Column(String(50), nullable=False)
    verdict_summary = Column(Text)
    kill_shot = Column(Text)
    scenarios = Column(JSON)  # Store all three scenarios as JSON
    steel_man = Column(Text)
    full_analysis = Column(Text, nullable=False)
    
    # Metadata
    ai_provider_used = Column(String(50))
    scraped_data = Column(JSON)  # Optional competitor intelligence
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "business_name": self.business_name,
            "idea_description": self.idea_description,
            "target_market": self.target_market,
            "revenue_model": self.revenue_model,
            "assumptions": self.assumptions,
            "competitive_landscape": self.competitive_landscape,
            "verdict": self.verdict,
            "verdict_summary": self.verdict_summary,
            "kill_shot": self.kill_shot,
            "scenarios": self.scenarios,
            "steel_man": self.steel_man,
            "full_analysis": self.full_analysis,
            "ai_provider_used": self.ai_provider_used,
            "scraped_data": self.scraped_data
        }


# Create engine and session
engine = create_engine(f"sqlite:///{config.DATABASE_PATH}", echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_database():
    """Initialize the database, creating all tables."""
    Base.metadata.create_all(engine)


def get_session():
    """Get a database session."""
    return SessionLocal()


