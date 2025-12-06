"""Web scraping functionality for competitor intelligence."""

import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
import time
from intelligence.sources import DataSources
import config


class WebScraper:
    """Web scraper for gathering competitor intelligence."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": DataSources.USER_AGENT})
        self._cache = {}
    
    def search_google(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Search Google using Serper API (if configured) or basic scraping.
        
        Args:
            query: Search query
            num_results: Number of results to return
        
        Returns:
            List of search results with title, snippet, and URL
        """
        # Check cache
        cache_key = f"google_{query}"
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        results = []
        
        # Try Serper API if configured
        if DataSources.SERPER_API_KEY:
            try:
                response = requests.post(
                    DataSources.SERPER_API_URL,
                    headers={
                        "X-API-KEY": DataSources.SERPER_API_KEY,
                        "Content-Type": "application/json"
                    },
                    json={"q": query, "num": num_results},
                    timeout=DataSources.TIMEOUT
                )
                
                if response.status_code == 200:
                    data = response.json()
                    for item in data.get("organic", [])[:num_results]:
                        results.append({
                            "title": item.get("title", ""),
                            "snippet": item.get("snippet", ""),
                            "url": item.get("link", "")
                        })
            except Exception as e:
                print(f"Serper API error: {e}")
        
        # Cache results
        if results:
            self._cache[cache_key] = results
        
        return results
    
    def scrape_webpage(self, url: str) -> Optional[str]:
        """
        Scrape text content from a webpage.
        
        Args:
            url: URL to scrape
        
        Returns:
            Text content or None if failed
        """
        try:
            response = self.session.get(url, timeout=DataSources.TIMEOUT)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = " ".join(chunk for chunk in chunks if chunk)
            
            return text[:5000]  # Limit to first 5000 chars
        
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None
    
    def gather_competitor_intelligence(
        self,
        business_data: Dict,
        max_sources: int = 5
    ) -> Dict:
        """
        Gather competitor intelligence for a business.
        
        Args:
            business_data: Business information
            max_sources: Maximum number of sources to scrape
        
        Returns:
            Dictionary with intelligence data
        """
        if not config.SCRAPING_ENABLED:
            return {"enabled": False, "error": "Scraping is disabled in config"}
        
        # Check if SERPER API key is configured
        if not DataSources.SERPER_API_KEY:
            return {
                "enabled": True,
                "sources": [],
                "timestamp": time.time(),
                "error": "SERPER_API_KEY not configured. Please set it in your .env file to enable competitor intelligence gathering."
            }
        
        intelligence = {
            "enabled": True,
            "sources": [],
            "timestamp": time.time()
        }
        
        # Generate search queries
        queries = DataSources.get_search_queries(business_data)
        
        if not queries:
            # If no queries generated, create basic ones from description
            description = business_data.get("description", "")
            name = business_data.get("name", "")
            
            if name:
                queries.append(f"{name} competitors")
                queries.append(f"{name} market analysis")
            
            if description:
                # Extract first few words as keywords
                words = description.split()[:10]
                key_phrase = " ".join(words)
                queries.append(f"{key_phrase} market")
                queries.append(f"{key_phrase} competitors")
        
        # Search and gather information
        for query in queries[:3]:  # Increase to first 3 queries
            try:
                results = self.search_google(query, num_results=max_sources)
                
                for result in results:
                    intelligence["sources"].append({
                        "query": query,
                        "title": result.get("title", ""),
                        "snippet": result.get("snippet", ""),
                        "url": result.get("url", "")
                    })
                
                time.sleep(1)  # Rate limiting
            except Exception as e:
                print(f"Error gathering intelligence for query '{query}': {e}")
                # Continue with other queries even if one fails
                continue
        
        # Add error message if no sources were found
        if not intelligence["sources"]:
            intelligence["error"] = "No competitor intelligence sources were found. This may be due to API rate limits or network issues."
        
        return intelligence
    
    def format_intelligence_for_prompt(self, intelligence: Dict) -> str:
        """
        Format intelligence data for inclusion in AI prompt.
        
        Args:
            intelligence: Intelligence data dictionary
        
        Returns:
            Formatted string
        """
        if not intelligence.get("enabled") or not intelligence.get("sources"):
            return ""
        
        formatted = "COMPETITOR & MARKET INTELLIGENCE:\n\n"
        
        for i, source in enumerate(intelligence["sources"][:10], 1):
            formatted += f"{i}. **{source['title']}**\n"
            formatted += f"   Query: {source['query']}\n"
            formatted += f"   {source['snippet']}\n"
            formatted += f"   Source: {source['url']}\n\n"
        
        return formatted

