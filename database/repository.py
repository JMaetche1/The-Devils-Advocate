"""Database operations for managing analyses."""

from typing import List, Optional
from datetime import datetime
from sqlalchemy import desc, or_
from database.models import Analysis, get_session, init_database
from analysis.framework import AnalysisResult


class AnalysisRepository:
    """Repository for analysis CRUD operations."""
    
    def __init__(self):
        """Initialize the repository and ensure database exists."""
        init_database()
    
    def save_analysis(
        self,
        business_data: dict,
        result: AnalysisResult,
        ai_provider: str,
        scraped_data: Optional[dict] = None
    ) -> Analysis:
        """
        Save an analysis to the database.
        
        Args:
            business_data: Original business input data
            result: Analysis result
            ai_provider: Name of AI provider used
            scraped_data: Optional competitor intelligence data
        
        Returns:
            Saved Analysis object
        """
        session = get_session()
        
        try:
            analysis = Analysis(
                business_name=business_data.get("name", "Unnamed"),
                idea_description=business_data.get("description", ""),
                target_market=business_data.get("target_market"),
                revenue_model=business_data.get("revenue_model"),
                assumptions=business_data.get("assumptions"),
                competitive_landscape=business_data.get("competitive_landscape"),
                verdict=result.verdict,
                verdict_summary=result.verdict_summary,
                kill_shot=result.kill_shot,
                scenarios={
                    "market": result.scenario_market,
                    "operations": result.scenario_operations,
                    "black_swan": result.scenario_black_swan
                },
                steel_man=result.steel_man,
                full_analysis=result.full_analysis,
                ai_provider_used=ai_provider,
                scraped_data=scraped_data
            )
            
            session.add(analysis)
            session.commit()
            session.refresh(analysis)
            
            return analysis
        finally:
            session.close()
    
    def get_all_analyses(self, limit: Optional[int] = None) -> List[Analysis]:
        """
        Get all analyses, ordered by most recent first.
        
        Args:
            limit: Optional limit on number of results
        
        Returns:
            List of Analysis objects
        """
        session = get_session()
        
        try:
            query = session.query(Analysis).order_by(desc(Analysis.timestamp))
            
            if limit:
                query = query.limit(limit)
            
            return query.all()
        finally:
            session.close()
    
    def get_analysis_by_id(self, analysis_id: int) -> Optional[Analysis]:
        """Get a specific analysis by ID."""
        session = get_session()
        
        try:
            return session.query(Analysis).filter(Analysis.id == analysis_id).first()
        finally:
            session.close()
    
    def search_analyses(self, query: str, limit: Optional[int] = 50) -> List[Analysis]:
        """
        Search analyses by business name or description.
        
        Args:
            query: Search query string
            limit: Maximum number of results
        
        Returns:
            List of matching Analysis objects
        """
        session = get_session()
        
        try:
            search_pattern = f"%{query}%"
            results = session.query(Analysis).filter(
                or_(
                    Analysis.business_name.ilike(search_pattern),
                    Analysis.idea_description.ilike(search_pattern)
                )
            ).order_by(desc(Analysis.timestamp)).limit(limit).all()
            
            return results
        finally:
            session.close()
    
    def filter_by_verdict(self, verdict: str) -> List[Analysis]:
        """Get all analyses with a specific verdict."""
        session = get_session()
        
        try:
            return session.query(Analysis).filter(
                Analysis.verdict == verdict.upper()
            ).order_by(desc(Analysis.timestamp)).all()
        finally:
            session.close()
    
    def delete_analysis(self, analysis_id: int) -> bool:
        """
        Delete an analysis by ID.
        
        Returns:
            True if deleted, False if not found
        """
        session = get_session()
        
        try:
            analysis = session.query(Analysis).filter(Analysis.id == analysis_id).first()
            
            if analysis:
                session.delete(analysis)
                session.commit()
                return True
            
            return False
        finally:
            session.close()
    
    def get_statistics(self) -> dict:
        """Get statistics about stored analyses."""
        session = get_session()
        
        try:
            total = session.query(Analysis).count()
            viable = session.query(Analysis).filter(Analysis.verdict == "VIABLE").count()
            risky = session.query(Analysis).filter(Analysis.verdict == "RISKY").count()
            doa = session.query(Analysis).filter(Analysis.verdict == "DEAD ON ARRIVAL").count()
            
            return {
                "total": total,
                "viable": viable,
                "risky": risky,
                "dead_on_arrival": doa
            }
        finally:
            session.close()


