"""Reusable UI components for Streamlit."""

import streamlit as st
from typing import Dict, Optional
from analysis.framework import AnalysisResult
from database.models import Analysis
from ui.styles import get_verdict_class


def render_header():
    """Render the application header."""
    st.markdown("""
        <div class="app-header">
            <h1>⚔️ The Devil's Advocate</h1>
            <p>Ruthless Red Team Business Analysis</p>
        </div>
    """, unsafe_allow_html=True)


def render_verdict(result: AnalysisResult):
    """Render the verdict section."""
    verdict_class = get_verdict_class(result.verdict)
    
    # Escape dollar signs to prevent LaTeX rendering issues
    verdict_summary = result.verdict_summary.replace('$', r'\$')
    
    st.markdown(f"""
        <div class="{verdict_class}">
            ⚖️ VERDICT: {result.verdict}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"**{verdict_summary}**")


def render_kill_shot(result: AnalysisResult):
    """Render the kill shot section."""
    st.markdown("""
        <div class="kill-shot">
            <h3>💀 THE "KILL SHOT" (The Fatal Flaw)</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Escape dollar signs to prevent LaTeX rendering issues
    kill_shot = result.kill_shot.replace('$', r'\$')
    st.markdown(kill_shot)


def render_scenarios(result: AnalysisResult):
    """Render the scenario simulation section."""
    st.markdown("### 🎯 SCENARIO SIMULATION (The Wargame)")
    
    # Escape dollar signs to prevent LaTeX rendering issues
    scenario_market = result.scenario_market.replace('$', r'\$')
    scenario_operations = result.scenario_operations.replace('$', r'\$')
    scenario_black_swan = result.scenario_black_swan.replace('$', r'\$')
    
    # Market scenario
    with st.expander("📊 Scenario A: The Market", expanded=True):
        st.markdown(scenario_market)
    
    # Operations scenario
    with st.expander("⚙️ Scenario B: The Operations", expanded=True):
        st.markdown(scenario_operations)
    
    # Black Swan scenario
    with st.expander("🦢 Scenario C: The Black Swan", expanded=True):
        st.markdown(scenario_black_swan)


def render_steel_man(result: AnalysisResult):
    """Render the steel man argument section."""
    st.markdown("""
        <div class="steel-man">
            <h3>🛡️ THE "STEEL MAN" ARGUMENT</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Escape dollar signs to prevent LaTeX rendering issues
    steel_man = result.steel_man.replace('$', r'\$')
    st.markdown(steel_man)


def render_full_analysis(result: AnalysisResult, competitor_data: dict = None):
    """Render the complete analysis in one view."""
    render_verdict(result)
    st.markdown("---")
    
    render_kill_shot(result)
    st.markdown("---")
    
    render_scenarios(result)
    st.markdown("---")
    
    render_steel_man(result)
    
    # Show competitor intelligence if it was gathered
    if competitor_data:
        st.markdown("---")
        render_competitor_intelligence(competitor_data)


def render_history_item(analysis: Analysis, key_prefix: str = ""):
    """Render a single history item."""
    verdict_emoji = {
        "VIABLE": "✅",
        "RISKY": "⚠️",
        "DEAD ON ARRIVAL": "❌"
    }.get(analysis.verdict, "❓")
    
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.markdown(f"**{verdict_emoji} {analysis.business_name}**")
        st.caption(analysis.idea_description[:100] + "...")
    
    with col2:
        st.caption(analysis.timestamp.strftime("%Y-%m-%d") if analysis.timestamp else "N/A")
    
    with col3:
        if st.button("View", key=f"{key_prefix}_view_{analysis.id}"):
            return analysis.id
    
    return None


def render_statistics(stats: Dict):
    """Render statistics dashboard."""
    st.markdown("### 📊 Analysis Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{stats['total']}</div>
                <div class="stat-label">Total Analyses</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number" style="color: #10b981;">{stats['viable']}</div>
                <div class="stat-label">Viable</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number" style="color: #f59e0b;">{stats['risky']}</div>
                <div class="stat-label">Risky</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number" style="color: #ef4444;">{stats['dead_on_arrival']}</div>
                <div class="stat-label">Dead on Arrival</div>
            </div>
        """, unsafe_allow_html=True)


def render_api_key_input(provider_name: str, configured: bool) -> Optional[str]:
    """Render API key input for a provider."""
    status = "✅ Configured" if configured else "❌ Not Configured"
    
    with st.expander(f"{provider_name} API Key - {status}"):
        if not configured:
            st.warning(f"Please enter your {provider_name} API key to use this provider.")
        
        api_key = st.text_input(
            f"{provider_name} API Key",
            type="password",
            key=f"api_key_{provider_name}",
            help=f"Enter your {provider_name} API key. It will not be stored permanently."
        )
        
        return api_key if api_key else None
    
    return None


def render_loading_message():
    """Render a loading animation with messages."""
    messages = [
        "🔍 Analyzing business model...",
        "💀 Identifying fatal flaws...",
        "🎯 Running scenario simulations...",
        "⚔️ Preparing ruthless critique...",
        "🔥 Stress-testing assumptions..."
    ]
    
    import random
    message = random.choice(messages)
    
    st.markdown(f"""
        <div class="loading" style="text-align: center; padding: 2rem;">
            <h3>{message}</h3>
        </div>
    """, unsafe_allow_html=True)


def render_competitor_intelligence(competitor_data: dict):
    """Render the competitor intelligence that was gathered."""
    st.markdown("### 🔍 Competitor Intelligence Gathered")
    
    if not competitor_data or not competitor_data.get("enabled"):
        st.info("No competitor intelligence was gathered for this analysis.")
        return
    
    # Check for error message
    if competitor_data.get("error"):
        st.error(f"⚠️ {competitor_data['error']}")
        if "SERPER_API_KEY" in competitor_data['error']:
            st.info("""
            **How to enable competitor intelligence:**
            
            1. Sign up for a free account at [serper.dev](https://serper.dev)
            2. Get your API key from the dashboard
            3. Add it to your `.env` file: `SERPER_API_KEY=your_key_here`
            4. Restart the application
            
            The free tier includes 2,500 searches per month.
            """)
        return
    
    sources = competitor_data.get("sources", [])
    
    if not sources:
        st.warning("Competitor intelligence gathering was enabled but no data was found.")
        return
    
    # Summary stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sources Found", len(sources))
    
    with col2:
        unique_urls = len(set(s.get('url', '') for s in sources))
        st.metric("Unique URLs", unique_urls)
    
    with col3:
        unique_queries = len(set(s.get('query', '') for s in sources))
        st.metric("Search Queries", unique_queries)
    
    st.markdown("---")
    
    # Show data sources in an expandable section
    with st.expander("📊 View All Intelligence Sources", expanded=False):
        for i, source in enumerate(sources, 1):
            st.markdown(f"""
            <div style="
                background-color: #1e293b;
                padding: 1rem;
                border-radius: 8px;
                margin: 0.5rem 0;
                border-left: 3px solid #3b82f6;
            ">
                <strong style="color: #60a5fa;">Source {i}: {source.get('title', 'Untitled')}</strong><br>
                <span style="color: #94a3b8; font-size: 0.9rem;">Query: <em>{source.get('query', 'N/A')}</em></span><br>
                <p style="margin: 0.5rem 0; color: #e2e8f0;">{source.get('snippet', 'No snippet available')}</p>
                <a href="{source.get('url', '#')}" target="_blank" style="color: #60a5fa; font-size: 0.85rem;">
                    🔗 {source.get('url', 'No URL')}
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    # Show the formatted intelligence text that was sent to AI
    st.markdown("#### 📝 Intelligence Summary Provided to AI")
    
    with st.expander("View Full Intelligence Context", expanded=False):
        # Group by query
        queries = {}
        for source in sources:
            query = source.get('query', 'Unknown')
            if query not in queries:
                queries[query] = []
            queries[query].append(source)
        
        for query, query_sources in queries.items():
            st.markdown(f"**Search Query:** `{query}`")
            st.caption(f"Found {len(query_sources)} results")
            
            for source in query_sources:
                st.markdown(f"- **{source.get('title', 'N/A')}**")
                st.markdown(f"  {source.get('snippet', 'No snippet')}")
                st.caption(f"  Source: {source.get('url', 'N/A')}")
                st.markdown("")
            
            st.markdown("---")
    
    # Show insights
    st.markdown("#### 💡 Intelligence Insights")
    
    # Analyze what was found
    titles = [s.get('title', '').lower() for s in sources]
    snippets = [s.get('snippet', '').lower() for s in sources]
    
    insights = []
    
    # Check for pricing info
    pricing_keywords = ['price', 'pricing', 'cost', '$', 'fee', 'subscription']
    if any(any(keyword in text for keyword in pricing_keywords) for text in titles + snippets):
        insights.append("💰 Pricing information was found in the competitive intelligence")
    
    # Check for competitor info
    competitor_keywords = ['competitor', 'alternative', 'vs', 'versus', 'comparison']
    if any(any(keyword in text for keyword in competitor_keywords) for text in titles + snippets):
        insights.append("🏢 Direct competitor information was gathered")
    
    # Check for market size/trends
    market_keywords = ['market', 'industry', 'trend', 'growth', 'size']
    if any(any(keyword in text for keyword in market_keywords) for text in titles + snippets):
        insights.append("📈 Market trends and industry data was collected")
    
    # Check for regulatory/legal
    legal_keywords = ['regulation', 'legal', 'compliance', 'law', 'policy']
    if any(any(keyword in text for keyword in legal_keywords) for text in titles + snippets):
        insights.append("⚖️ Regulatory or legal information was discovered")
    
    # Check for reviews/sentiment
    review_keywords = ['review', 'rating', 'feedback', 'customer', 'user']
    if any(any(keyword in text for keyword in review_keywords) for text in titles + snippets):
        insights.append("⭐ Customer reviews or feedback was found")
    
    if insights:
        for insight in insights:
            st.success(insight)
    else:
        st.info("General competitive information was gathered")
    
    st.caption("ℹ️ This intelligence was used to enhance the analysis above with real-world competitive data.")

