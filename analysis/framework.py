"""Pre-Mortem analysis framework implementation."""

import re
from typing import Dict, Optional
from dataclasses import dataclass


@dataclass
class AnalysisResult:
    """Structured result of a business analysis."""
    verdict: str  # VIABLE, RISKY, or DEAD ON ARRIVAL
    verdict_summary: str
    kill_shot: str
    scenario_market: str
    scenario_operations: str
    scenario_black_swan: str
    steel_man: str
    full_analysis: str
    raw_response: str


def parse_analysis(raw_response: str) -> AnalysisResult:
    """Parse the AI response into structured components."""
    
    # Initialize with defaults
    verdict = "UNKNOWN"
    verdict_summary = ""
    kill_shot = ""
    scenario_market = ""
    scenario_operations = ""
    scenario_black_swan = ""
    steel_man = ""
    
    # Extract verdict
    verdict_match = re.search(
        r'\*\*1\.\s*THE VERDICT\*\*\s*\n\s*\[?(VIABLE|RISKY|DEAD ON ARRIVAL)\]?(.+?)(?=\*\*2\.|$)',
        raw_response,
        re.IGNORECASE | re.DOTALL
    )
    if verdict_match:
        verdict = verdict_match.group(1).upper()
        verdict_summary = verdict_match.group(2).strip()
    
    # Extract kill shot
    kill_shot_match = re.search(
        r'\*\*2\.\s*THE "KILL SHOT".*?\*\*\s*\n(.+?)(?=\*\*3\.|$)',
        raw_response,
        re.IGNORECASE | re.DOTALL
    )
    if kill_shot_match:
        kill_shot = kill_shot_match.group(1).strip()
    
    # Extract scenarios
    scenario_section = re.search(
        r'\*\*3\.\s*SCENARIO SIMULATION.*?\*\*(.+?)(?=\*\*4\.|$)',
        raw_response,
        re.IGNORECASE | re.DOTALL
    )
    
    if scenario_section:
        scenarios_text = scenario_section.group(1)
        
        # Market scenario
        market_match = re.search(
            r'\*\s*\*\*Scenario A \(The Market\):\*\*(.+?)(?=\*\s*\*\*Scenario [BC]|$)',
            scenarios_text,
            re.IGNORECASE | re.DOTALL
        )
        if market_match:
            scenario_market = market_match.group(1).strip()
        
        # Operations scenario
        ops_match = re.search(
            r'\*\s*\*\*Scenario B \(The Operations\):\*\*(.+?)(?=\*\s*\*\*Scenario C|$)',
            scenarios_text,
            re.IGNORECASE | re.DOTALL
        )
        if ops_match:
            scenario_operations = ops_match.group(1).strip()
        
        # Black Swan scenario
        swan_match = re.search(
            r'\*\s*\*\*Scenario C \(The Black Swan\):\*\*(.+?)(?=\n\n|$)',
            scenarios_text,
            re.IGNORECASE | re.DOTALL
        )
        if swan_match:
            scenario_black_swan = swan_match.group(1).strip()
    
    # Extract Steel Man
    steel_man_match = re.search(
        r'\*\*4\.\s*THE "STEEL MAN" ARGUMENT\*\*\s*\n(.+?)$',
        raw_response,
        re.IGNORECASE | re.DOTALL
    )
    if steel_man_match:
        steel_man = steel_man_match.group(1).strip()
    
    # Format full analysis
    full_analysis = raw_response
    
    return AnalysisResult(
        verdict=verdict,
        verdict_summary=verdict_summary,
        kill_shot=kill_shot,
        scenario_market=scenario_market,
        scenario_operations=scenario_operations,
        scenario_black_swan=scenario_black_swan,
        steel_man=steel_man,
        full_analysis=full_analysis,
        raw_response=raw_response
    )


def validate_analysis(result: AnalysisResult) -> bool:
    """Validate that the analysis has all required components."""
    required_fields = [
        result.verdict,
        result.verdict_summary,
        result.kill_shot,
        result.scenario_market,
        result.scenario_operations,
        result.scenario_black_swan,
        result.steel_man
    ]
    
    # Check all fields exist and are not empty
    if not all(field.strip() for field in required_fields):
        return False
    
    # Check minimum length requirements for quality
    # Kill shot should be substantial (at least 200 chars)
    if len(result.kill_shot.strip()) < 200:
        return False
    
    # Each scenario should be detailed (at least 150 chars each)
    if len(result.scenario_market.strip()) < 150:
        return False
    if len(result.scenario_operations.strip()) < 150:
        return False
    if len(result.scenario_black_swan.strip()) < 150:
        return False
    
    # Steel man should be actionable (at least 200 chars)
    if len(result.steel_man.strip()) < 200:
        return False
    
    return True

