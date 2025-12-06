"""Data source configurations for competitor intelligence."""

import config


class DataSources:
    """Configuration for various data sources."""
    
    # Google Search API (via Serper or similar)
    SERPER_API_URL = "https://google.serper.dev/search"
    SERPER_API_KEY = config.SERPER_API_KEY
    
    # User agent for web scraping
    USER_AGENT = config.USER_AGENT
    
    # Timeout settings
    TIMEOUT = config.SCRAPING_TIMEOUT
    
    # Cache duration
    CACHE_DURATION = config.CACHE_DURATION
    
    @staticmethod
    def get_search_queries(business_data: dict) -> list:
        """
        Generate search queries based on business data.
        
        Args:
            business_data: Business information
        
        Returns:
            List of search query strings
        """
        queries = []
        
        business_name = business_data.get("name", "")
        target_market = business_data.get("target_market", "")
        description = business_data.get("description", "")
        revenue_model = business_data.get("revenue_model", "")
        competitive_landscape = business_data.get("competitive_landscape", "")
        
        # Priority 1: Direct competitive queries
        if business_name and business_name.lower() not in ["quick analysis", "unnamed", "uploaded document analysis"]:
            queries.append(f"{business_name} competitors analysis")
            queries.append(f"{business_name} market pricing")
            queries.append(f"{business_name} customer reviews")
        
        # Priority 2: Market and industry queries
        if target_market and target_market.lower() != "not specified":
            queries.append(f"{target_market} market size 2024")
            queries.append(f"{target_market} industry trends")
            queries.append(f"{target_market} competitive landscape")
        
        # Priority 3: Extract keywords from description
        if description:
            # Extract meaningful keywords (nouns, longer words)
            words = [w for w in description.split() if len(w) > 4][:8]
            if words:
                key_phrase = " ".join(words[:5])
                queries.append(f"{key_phrase} market competitors")
                queries.append(f"{key_phrase} industry analysis")
        
        # Priority 4: Revenue model research
        if revenue_model and revenue_model.lower() != "not specified":
            rev_words = [w for w in revenue_model.split() if len(w) > 3][:5]
            if rev_words:
                rev_phrase = " ".join(rev_words)
                queries.append(f"{rev_phrase} pricing benchmarks")
        
        # Priority 5: Known competitors
        if competitive_landscape and competitive_landscape.lower() not in ["not specified", "none", ""]:
            # Extract competitor names (simple heuristic)
            comp_words = competitive_landscape.split()[:10]
            if comp_words:
                queries.append(f"{' '.join(comp_words[:5])} market analysis")
        
        # Fallback: Generic business analysis queries
        if not queries:
            queries.append("startup market analysis 2024")
            queries.append("business model competitors")
            queries.append("industry trends 2024")
        
        return queries

