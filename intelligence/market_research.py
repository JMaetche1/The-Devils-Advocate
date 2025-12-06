"""Market research and analysis tools."""

from typing import Dict, List
from intelligence.web_scraper import WebScraper


class MarketResearcher:
    """Conducts market research for business analysis."""
    
    def __init__(self):
        self.scraper = WebScraper()
    
    def research_market(self, business_data: Dict) -> Dict:
        """
        Conduct comprehensive market research.
        
        Args:
            business_data: Business information
        
        Returns:
            Dictionary with market research data
        """
        research = {
            "competitor_intelligence": None,
            "market_trends": [],
            "regulatory_info": []
        }
        
        # Gather competitor intelligence
        try:
            intelligence = self.scraper.gather_competitor_intelligence(business_data)
            research["competitor_intelligence"] = intelligence
        except Exception as e:
            print(f"Error gathering competitor intelligence: {e}")
        
        return research
    
    def format_research_for_analysis(self, research: Dict) -> str:
        """
        Format research data for AI analysis.
        
        Args:
            research: Market research dictionary
        
        Returns:
            Formatted string for prompt
        """
        if not research.get("competitor_intelligence"):
            return ""
        
        return self.scraper.format_intelligence_for_prompt(
            research["competitor_intelligence"]
        )


