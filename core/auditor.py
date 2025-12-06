"""Main AI auditor logic for business analysis."""

from typing import Dict, Optional, Tuple
from core.ai_providers import AIProvider, get_provider
from core.prompts import THE_AUDITOR_SYSTEM_PROMPT, get_analysis_prompt
from analysis.framework import parse_analysis, validate_analysis, AnalysisResult
from core.usage_tracker import calculate_cost
from database.usage_models import save_usage_record, init_usage_database
import config

# Initialize usage database
init_usage_database()


class Auditor:
    """The Auditor - ruthless business plan analyzer."""
    
    def __init__(self, provider_name: str = None, model: str = None, api_key: Optional[str] = None):
        """Initialize the auditor with an AI provider and optional model."""
        provider_name = provider_name or config.DEFAULT_AI_PROVIDER
        self.provider: AIProvider = get_provider(provider_name, api_key, model)
        self.provider_name = provider_name
    
    def analyze(
        self,
        business_data: Dict,
        competitor_intelligence: Optional[str] = None,
        temperature: float = None,
        max_tokens: int = None,
        analysis_id: Optional[int] = None
    ) -> Tuple[AnalysisResult, Dict]:
        """
        Perform a ruthless analysis of a business idea.
        
        Args:
            business_data: Dictionary containing business information:
                - name: Business name/concept
                - description: Full description
                - target_market: Target market description
                - revenue_model: How it makes money
                - assumptions: Key assumptions
                - competitive_landscape: Competition info
            competitor_intelligence: Optional scraped competitor data
            temperature: AI temperature (default from config)
            max_tokens: Max response tokens (default from config)
            analysis_id: Optional ID to link usage to analysis
        
        Returns:
            Tuple of (AnalysisResult, usage_dict)
        """
        if not self.provider.is_configured():
            raise ValueError(
                f"AI provider '{self.provider_name}' is not configured. "
                f"Please set the appropriate API key."
            )
        
        # Use defaults if not specified
        temperature = temperature or config.DEFAULT_TEMPERATURE
        max_tokens = max_tokens or config.DEFAULT_MAX_TOKENS
        
        # Generate prompts
        system_prompt = THE_AUDITOR_SYSTEM_PROMPT
        user_prompt = get_analysis_prompt(business_data, competitor_intelligence)
        
        # Get AI response with usage tracking
        raw_response, usage = self.provider.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Calculate costs
        cost_usd, cost_cad = calculate_cost(
            self.provider_name,
            usage['model'],
            usage['input_tokens'],
            usage['output_tokens']
        )
        
        # Save usage to database
        save_usage_record(
            provider=self.provider_name,
            model=usage['model'],
            input_tokens=usage['input_tokens'],
            output_tokens=usage['output_tokens'],
            cost_usd=cost_usd,
            cost_cad=cost_cad,
            analysis_id=analysis_id
        )
        
        # Add cost info to usage dict
        usage['cost_usd'] = cost_usd
        usage['cost_cad'] = cost_cad
        
        # Parse and validate
        result = parse_analysis(raw_response)
        
        if not validate_analysis(result):
            # If validation fails, still return what we got
            # but mark it in the verdict
            result.verdict = "INCOMPLETE"
            result.verdict_summary = (
                "Analysis incomplete. The AI response did not follow the expected format. "
                "Check the full analysis below."
            )
        
        return result, usage
    
    def quick_check(self, business_description: str) -> Tuple[AnalysisResult, Dict]:
        """
        Quick analysis with minimal input.
        
        Args:
            business_description: Brief description of the business idea
        
        Returns:
            Tuple of (AnalysisResult, usage_dict)
        """
        business_data = {
            "name": "Quick Analysis",
            "description": business_description,
            "target_market": "Not specified",
            "revenue_model": "Not specified",
            "assumptions": "None provided",
            "competitive_landscape": "Not specified"
        }
        
        return self.analyze(business_data)

