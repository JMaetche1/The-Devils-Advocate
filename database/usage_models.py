"""Database models for API usage tracking."""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import config
from database.models import Base, engine, SessionLocal

# Use the same Base as models.py


class APIUsage(Base):
    """Model for storing API usage records."""
    
    __tablename__ = "api_usage"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.now, nullable=False)
    provider = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    input_tokens = Column(Integer, nullable=False)
    output_tokens = Column(Integer, nullable=False)
    total_tokens = Column(Integer, nullable=False)
    cost_usd = Column(Float, nullable=False)
    cost_cad = Column(Float, nullable=False)
    analysis_id = Column(Integer, ForeignKey('analyses.id'), nullable=True)
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "provider": self.provider,
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "cost_usd": self.cost_usd,
            "cost_cad": self.cost_cad,
            "analysis_id": self.analysis_id
        }


def init_usage_database():
    """Initialize the usage tracking database."""
    Base.metadata.create_all(engine)


def save_usage_record(
    provider: str,
    model: str,
    input_tokens: int,
    output_tokens: int,
    cost_usd: float,
    cost_cad: float,
    analysis_id: int = None
):
    """Save a usage record to the database."""
    session = SessionLocal()
    try:
        usage = APIUsage(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            cost_usd=cost_usd,
            cost_cad=cost_cad,
            analysis_id=analysis_id
        )
        session.add(usage)
        session.commit()
        return usage
    finally:
        session.close()


def get_usage_stats(days: int = None):
    """Get usage statistics from database."""
    from sqlalchemy import func
    from datetime import datetime, timedelta
    
    session = SessionLocal()
    try:
        query = session.query(
            func.count(APIUsage.id).label('total_calls'),
            func.sum(APIUsage.input_tokens).label('total_input'),
            func.sum(APIUsage.output_tokens).label('total_output'),
            func.sum(APIUsage.total_tokens).label('total_tokens'),
            func.sum(APIUsage.cost_usd).label('total_usd'),
            func.sum(APIUsage.cost_cad).label('total_cad')
        )
        
        if days:
            cutoff = datetime.now() - timedelta(days=days)
            query = query.filter(APIUsage.timestamp >= cutoff)
        
        result = query.first()
        
        # Get by provider
        provider_query = session.query(
            APIUsage.provider,
            func.count(APIUsage.id).label('calls'),
            func.sum(APIUsage.total_tokens).label('tokens'),
            func.sum(APIUsage.cost_cad).label('cost')
        ).group_by(APIUsage.provider)
        
        if days:
            cutoff = datetime.now() - timedelta(days=days)
            provider_query = provider_query.filter(APIUsage.timestamp >= cutoff)
        
        by_provider = {}
        for row in provider_query.all():
            by_provider[row.provider] = {
                "calls": row.calls or 0,
                "tokens": row.tokens or 0,
                "cost_cad": float(row.cost or 0)
            }
        
        return {
            "total_calls": result.total_calls or 0,
            "total_input_tokens": result.total_input or 0,
            "total_output_tokens": result.total_output or 0,
            "total_tokens": result.total_tokens or 0,
            "total_cost_usd": float(result.total_usd or 0),
            "total_cost_cad": float(result.total_cad or 0),
            "by_provider": by_provider
        }
    finally:
        session.close()


def get_recent_usage(limit: int = 20):
    """Get recent usage records."""
    session = SessionLocal()
    try:
        records = session.query(APIUsage).order_by(
            APIUsage.timestamp.desc()
        ).limit(limit).all()
        return records
    finally:
        session.close()


