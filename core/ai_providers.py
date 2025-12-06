"""Multi-provider AI interface for The Devil's Advocate."""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Tuple
import os
from tenacity import retry, stop_after_attempt, wait_exponential

import config


class AIProvider(ABC):
    """Abstract base class for AI providers."""
    
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str, 
                 temperature: float = 0.8, max_tokens: int = 4000) -> Tuple[str, Dict]:
        """
        Generate a response from the AI provider.
        
        Returns:
            Tuple of (response_text, usage_dict)
            usage_dict contains: {
                'input_tokens': int,
                'output_tokens': int,
                'model': str
            }
        """
        pass
    
    @abstractmethod
    def is_configured(self) -> bool:
        """Check if the provider is properly configured with API key."""
        pass


class OpenAIProvider(AIProvider):
    """OpenAI GPT provider."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        self.api_key = api_key or config.OPENAI_API_KEY
        self.model = model
        self._client = None
    
    def _get_client(self):
        """Lazy load the OpenAI client."""
        if self._client is None:
            from openai import OpenAI
            self._client = OpenAI(api_key=self.api_key)
        return self._client
    
    def is_configured(self) -> bool:
        return bool(self.api_key)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def generate(self, system_prompt: str, user_prompt: str,
                 temperature: float = 0.8, max_tokens: int = 4000) -> Tuple[str, Dict]:
        """Generate response using OpenAI."""
        if not self.is_configured():
            raise ValueError("OpenAI API key not configured")
        
        client = self._get_client()
        
        # GPT-5 and GPT-4.1 use different parameters than older models
        is_gpt5_series = self.model.startswith(('gpt-5', 'gpt-4.1'))
        
        # Build request parameters
        request_params = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
        }
        
        # GPT-5 models only support temperature=1 (default), so don't set it
        # Older models support custom temperature
        if not is_gpt5_series:
            request_params["temperature"] = temperature
        
        # Add the appropriate token limit parameter
        if is_gpt5_series:
            request_params["max_completion_tokens"] = max_tokens
        else:
            request_params["max_tokens"] = max_tokens
        
        response = client.chat.completions.create(**request_params)
        
        # Extract usage information
        usage = {
            'input_tokens': response.usage.prompt_tokens,
            'output_tokens': response.usage.completion_tokens,
            'model': self.model
        }
        
        return response.choices[0].message.content, usage


class AnthropicProvider(AIProvider):
    """Anthropic Claude provider."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        self.api_key = api_key or config.ANTHROPIC_API_KEY
        self.model = model
        self._client = None
    
    def _get_client(self):
        """Lazy load the Anthropic client."""
        if self._client is None:
            from anthropic import Anthropic
            self._client = Anthropic(api_key=self.api_key)
        return self._client
    
    def is_configured(self) -> bool:
        return bool(self.api_key)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def generate(self, system_prompt: str, user_prompt: str,
                 temperature: float = 0.8, max_tokens: int = 4000) -> Tuple[str, Dict]:
        """Generate response using Anthropic Claude."""
        if not self.is_configured():
            raise ValueError("Anthropic API key not configured")
        
        client = self._get_client()
        response = client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        
        # Extract usage information
        usage = {
            'input_tokens': response.usage.input_tokens,
            'output_tokens': response.usage.output_tokens,
            'model': self.model
        }
        
        return response.content[0].text, usage


class GoogleProvider(AIProvider):
    """Google Gemini provider."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-1.5-pro"):
        self.api_key = api_key or config.GOOGLE_API_KEY
        self.model = model
        self._client = None
    
    def _get_client(self):
        """Lazy load the Google client."""
        if self._client is None:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self._client = genai.GenerativeModel(self.model)
        return self._client
    
    def is_configured(self) -> bool:
        return bool(self.api_key)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def generate(self, system_prompt: str, user_prompt: str,
                 temperature: float = 0.8, max_tokens: int = 4000) -> Tuple[str, Dict]:
        """Generate response using Google Gemini."""
        if not self.is_configured():
            raise ValueError("Google API key not configured")
        
        client = self._get_client()
        
        # Gemini doesn't have separate system/user prompts, so combine them
        combined_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        response = client.generate_content(
            combined_prompt,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens,
            }
        )
        
        # Extract usage information (if available)
        usage = {
            'input_tokens': getattr(response.usage_metadata, 'prompt_token_count', 0),
            'output_tokens': getattr(response.usage_metadata, 'candidates_token_count', 0),
            'model': self.model
        }
        
        return response.text, usage


def get_provider(provider_name: str, api_key: Optional[str] = None, model: Optional[str] = None) -> AIProvider:
    """Factory function to get the appropriate AI provider."""
    providers = {
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
        "google": GoogleProvider,
    }
    
    provider_class = providers.get(provider_name.lower())
    if not provider_class:
        raise ValueError(f"Unknown provider: {provider_name}")
    
    # Initialize with model if provided
    if model:
        return provider_class(api_key=api_key, model=model)
    return provider_class(api_key=api_key)


def get_available_providers() -> Dict[str, Dict[str, Any]]:
    """Get list of available providers and their configuration status."""
    providers = {
        "openai": {
            "name": "OpenAI",
            "provider": OpenAIProvider(),
            "models": [
                "gpt-5.1",
                "gpt-5-pro",
                "gpt-5",
                "gpt-5-mini",
                "gpt-5-nano",
                "gpt-4.1",
                "gpt-4o",
                "gpt-4o-mini", 
                "gpt-4-turbo",
                "gpt-4",
                "gpt-3.5-turbo"
            ]
        },
        "anthropic": {
            "name": "Anthropic Claude",
            "provider": AnthropicProvider(),
            "models": [
                "claude-opus-4-5",
                "claude-opus-4-5-20251101",
                "claude-sonnet-4-5",
                "claude-haiku-4-5",
                "claude-3-7-sonnet-latest",
                "claude-3-7-sonnet-20250219",
                "claude-3-5-haiku-latest",
                "claude-3-5-sonnet-20241022",
                "claude-3-opus-20240229"
            ]
        },
        "google": {
            "name": "Google Gemini",
            "provider": GoogleProvider(),
            "models": [
                "gemini-3-pro",
                "gemini-2.5-pro",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-2.0-flash",
                "gemini-2.0-flash-exp",
                "gemini-2.0-flash-lite",
                "gemini-1.5-pro",
                "gemini-1.5-flash",
                "gemini-1.5-flash-8b",
                "gemini-1.5-pro-latest"
            ]
        }
    }
    
    for key, info in providers.items():
        info["configured"] = info["provider"].is_configured()
    
    return providers

