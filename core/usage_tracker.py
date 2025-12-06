"""API usage tracking and cost calculation."""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass
import json


@dataclass
class UsageRecord:
    """Record of a single API call."""
    timestamp: datetime
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    cost_cad: float
    analysis_id: Optional[int] = None


# Current pricing as of December 2024 (USD per 1M tokens)
# Updated with latest models including GPT-5 and Gemini 3
USD_TO_CAD_RATE = 1.36  # Keep updated with current exchange rate

PRICING = {
    "openai": {
        # GPT-5 series (estimates - verify with actual pricing when available)
        "gpt-5.1": {"input": 5.00, "output": 15.00},
        "gpt-5-pro": {"input": 8.00, "output": 25.00},
        "gpt-5": {"input": 5.00, "output": 15.00},
        "gpt-5-mini": {"input": 1.00, "output": 3.00},
        "gpt-5-nano": {"input": 0.50, "output": 1.50},
        "gpt-4.1": {"input": 4.00, "output": 12.00},
        # GPT-4 series (confirmed pricing)
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "gpt-4-turbo": {"input": 10.00, "output": 30.00},
        "gpt-4": {"input": 30.00, "output": 60.00},
        "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
    },
    "anthropic": {
        # Claude 4.x models (confirmed pricing from docs)
        "claude-opus-4-5": {"input": 5.00, "output": 25.00},
        "claude-opus-4-5-20251101": {"input": 5.00, "output": 25.00},
        "claude-sonnet-4-5": {"input": 3.00, "output": 15.00},
        "claude-haiku-4-5": {"input": 1.00, "output": 5.00},
        "claude-3-7-sonnet-latest": {"input": 3.00, "output": 15.00},
        "claude-3-7-sonnet-20250219": {"input": 3.00, "output": 15.00},
        "claude-3-5-haiku-latest": {"input": 0.80, "output": 4.00},
        # Claude 3.x models
        "claude-3-5-sonnet-20241022": {"input": 3.00, "output": 15.00},
        "claude-3-opus-20240229": {"input": 15.00, "output": 75.00},
        "claude-3-sonnet-20240229": {"input": 3.00, "output": 15.00},
        "claude-3-haiku-20240307": {"input": 0.25, "output": 1.25},
    },
    "google": {
        # Gemini 3.x models (estimates - verify with actual pricing)
        "gemini-3-pro": {"input": 2.00, "output": 7.00},
        # Gemini 2.5.x models
        "gemini-2.5-pro": {"input": 1.25, "output": 5.00},
        "gemini-2.5-flash": {"input": 0.60, "output": 2.50},
        "gemini-2.5-flash-lite": {"input": 0.40, "output": 1.50},
        # Gemini 2.x models
        "gemini-2.0-flash": {"input": 0.50, "output": 2.00},
        "gemini-2.0-flash-exp": {"input": 0.50, "output": 2.00},
        "gemini-2.0-flash-lite": {"input": 0.30, "output": 1.20},
        # Gemini 1.x models
        "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
        "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
        "gemini-1.5-flash-8b": {"input": 0.038, "output": 0.15},
        "gemini-1.5-pro-latest": {"input": 1.25, "output": 5.00},
        "gemini-pro": {"input": 0.50, "output": 1.50},
    }
}

# USD to CAD exchange rate (update periodically or use API)
USD_TO_CAD_RATE = 1.36  # As of December 2024


def calculate_cost(provider: str, model: str, input_tokens: int, output_tokens: int) -> tuple[float, float]:
    """
    Calculate cost for API usage.
    
    Args:
        provider: AI provider name
        model: Model name
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
    
    Returns:
        Tuple of (cost_usd, cost_cad)
    """
    provider_lower = provider.lower()
    
    # Get pricing for this model
    if provider_lower not in PRICING:
        return 0.0, 0.0
    
    model_pricing = PRICING[provider_lower].get(model)
    if not model_pricing:
        # Try to find a matching model (handle variations)
        for pricing_model, prices in PRICING[provider_lower].items():
            if pricing_model in model or model in pricing_model:
                model_pricing = prices
                break
    
    if not model_pricing:
        return 0.0, 0.0
    
    # Calculate cost (pricing is per 1M tokens)
    input_cost = (input_tokens / 1_000_000) * model_pricing["input"]
    output_cost = (output_tokens / 1_000_000) * model_pricing["output"]
    total_usd = input_cost + output_cost
    total_cad = total_usd * USD_TO_CAD_RATE
    
    return total_usd, total_cad


def estimate_tokens(text: str) -> int:
    """
    Estimate token count from text.
    Rule of thumb: ~4 characters per token for English text.
    
    Args:
        text: Text to estimate
    
    Returns:
        Estimated token count
    """
    return len(text) // 4


class UsageTracker:
    """Track API usage and costs."""
    
    def __init__(self):
        self.records: List[UsageRecord] = []
    
    def track_usage(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        analysis_id: Optional[int] = None
    ) -> UsageRecord:
        """
        Track a single API usage.
        
        Args:
            provider: AI provider name
            model: Model used
            input_tokens: Input token count
            output_tokens: Output token count
            analysis_id: Optional ID of the analysis
        
        Returns:
            UsageRecord
        """
        cost_usd, cost_cad = calculate_cost(provider, model, input_tokens, output_tokens)
        
        record = UsageRecord(
            timestamp=datetime.now(),
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=cost_usd,
            cost_cad=cost_cad,
            analysis_id=analysis_id
        )
        
        self.records.append(record)
        return record
    
    def get_total_usage(self, days: Optional[int] = None) -> Dict:
        """
        Get total usage statistics.
        
        Args:
            days: Optional number of days to look back
        
        Returns:
            Dictionary with usage statistics
        """
        records = self.records
        
        if days:
            cutoff = datetime.now() - timedelta(days=days)
            records = [r for r in records if r.timestamp >= cutoff]
        
        if not records:
            return {
                "total_calls": 0,
                "total_input_tokens": 0,
                "total_output_tokens": 0,
                "total_tokens": 0,
                "total_cost_usd": 0.0,
                "total_cost_cad": 0.0,
                "by_provider": {}
            }
        
        total_input = sum(r.input_tokens for r in records)
        total_output = sum(r.output_tokens for r in records)
        total_cost_usd = sum(r.cost_usd for r in records)
        total_cost_cad = sum(r.cost_cad for r in records)
        
        # Break down by provider
        by_provider = {}
        for record in records:
            if record.provider not in by_provider:
                by_provider[record.provider] = {
                    "calls": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost_usd": 0.0,
                    "cost_cad": 0.0
                }
            
            by_provider[record.provider]["calls"] += 1
            by_provider[record.provider]["input_tokens"] += record.input_tokens
            by_provider[record.provider]["output_tokens"] += record.output_tokens
            by_provider[record.provider]["cost_usd"] += record.cost_usd
            by_provider[record.provider]["cost_cad"] += record.cost_cad
        
        return {
            "total_calls": len(records),
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "total_tokens": total_input + total_output,
            "total_cost_usd": total_cost_usd,
            "total_cost_cad": total_cost_cad,
            "by_provider": by_provider
        }
    
    def get_recent_usage(self, limit: int = 10) -> List[UsageRecord]:
        """Get recent usage records."""
        return sorted(self.records, key=lambda x: x.timestamp, reverse=True)[:limit]
    
    def export_usage(self) -> str:
        """Export usage data as JSON."""
        data = []
        for record in self.records:
            data.append({
                "timestamp": record.timestamp.isoformat(),
                "provider": record.provider,
                "model": record.model,
                "input_tokens": record.input_tokens,
                "output_tokens": record.output_tokens,
                "cost_usd": record.cost_usd,
                "cost_cad": record.cost_cad,
                "analysis_id": record.analysis_id
            })
        return json.dumps(data, indent=2)
    
    def clear_old_records(self, days: int = 90):
        """Clear records older than specified days."""
        cutoff = datetime.now() - timedelta(days=days)
        self.records = [r for r in self.records if r.timestamp >= cutoff]


# Global tracker instance
_global_tracker = UsageTracker()


def get_tracker() -> UsageTracker:
    """Get the global usage tracker instance."""
    return _global_tracker

