"""Configuration management for The Devil's Advocate application."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# Database
DATABASE_PATH = DATA_DIR / "history.db"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")

# AI Provider Settings
DEFAULT_AI_PROVIDER = "openai"
DEFAULT_TEMPERATURE = 0.8
DEFAULT_MAX_TOKENS = 8000  # Increased for more detailed analysis

# Scraping Settings
SCRAPING_ENABLED = True
SCRAPING_TIMEOUT = 30  # seconds
CACHE_DURATION = 86400  # 24 hours in seconds
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# UI Settings
APP_TITLE = "The Devil's Advocate"
APP_SUBTITLE = "Red Team Business Analysis"
THEME = "dark"

