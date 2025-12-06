"""The Devil's Advocate - Main Streamlit Application."""

import streamlit as st
from typing import Optional
import traceback

# Import modules
from core.auditor import Auditor
from core.ai_providers import get_available_providers
from database.repository import AnalysisRepository
from database.usage_models import get_usage_stats, get_recent_usage
from intelligence.market_research import MarketResearcher
from analysis.report_generator import generate_markdown_report
from ui.components import (
    render_header,
    render_full_analysis,
    render_api_key_input,
    render_statistics,
    render_history_item,
    render_loading_message
)
from ui.usage_components import (
    render_usage_dashboard,
    render_usage_summary_card,
    render_recent_usage_table,
    render_cost_estimator,
    render_usage_alert
)
from ui.styles import get_custom_css
import config

# Page config
st.set_page_config(
    page_title="The Devil's Advocate",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize session state
if "current_analysis" not in st.session_state:
    st.session_state.current_analysis = None
if "show_history" not in st.session_state:
    st.session_state.show_history = False
if "selected_history_id" not in st.session_state:
    st.session_state.selected_history_id = None
if "business_data" not in st.session_state:
    st.session_state.business_data = {}
if "last_usage" not in st.session_state:
    st.session_state.last_usage = None
if "competitor_data" not in st.session_state:
    st.session_state.competitor_data = None

# Initialize repository
repo = AnalysisRepository()


def main():
    """Main application function."""
    
    # Render header
    render_header()
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🎯 Navigation")
        
        page = st.radio(
            "Select Page",
            ["New Analysis", "History", "Usage & Costs", "Settings"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Quick usage stats in sidebar
        usage_stats = get_usage_stats()
        if usage_stats["total_calls"] > 0:
            st.markdown("### 💰 Session Costs")
            st.metric("Total Spent (CAD)", f"${usage_stats['total_cost_cad']:.2f}")
            st.metric("API Calls", usage_stats["total_calls"])
            
            # Show alert if costs are high
            if usage_stats['total_cost_cad'] >= 5.0:
                st.caption("⚠️ Check Usage & Costs page")
        
        st.markdown("---")
        
        # Statistics
        stats = repo.get_statistics()
        if stats["total"] > 0:
            st.markdown("### 📊 Quick Stats")
            st.metric("Total Analyses", stats["total"])
            st.metric("Viable", stats["viable"], delta_color="normal")
            st.metric("Risky", stats["risky"], delta_color="off")
            st.metric("Dead on Arrival", stats["dead_on_arrival"], delta_color="inverse")
    
    # Route to appropriate page
    if page == "New Analysis":
        show_analysis_page()
    elif page == "History":
        show_history_page()
    elif page == "Usage & Costs":
        show_usage_page()
    elif page == "Settings":
        show_settings_page()


def show_analysis_page():
    """Show the main analysis input page."""
    
    st.markdown("## 📝 Business Analysis Input")
    
    # Check if viewing a previous analysis
    if st.session_state.selected_history_id:
        show_previous_analysis()
        return
    
    # Input mode selection
    input_mode = st.radio(
        "Input Mode",
        ["Structured Form", "Quick Analysis", "Upload Document"],
        horizontal=True
    )
    
    st.markdown("---")
    
    business_data = {}
    
    if input_mode == "Structured Form":
        business_data = show_structured_form()
    elif input_mode == "Quick Analysis":
        business_data = show_quick_form()
    elif input_mode == "Upload Document":
        business_data = show_upload_form()
    
    # AI Provider selection
    st.markdown("### 🤖 AI Provider & Model Selection")
    
    providers = get_available_providers()
    configured_providers = {k: v for k, v in providers.items() if v["configured"]}
    
    if not configured_providers:
        st.error("⚠️ No AI providers configured. Please set up at least one API key in Settings.")
        return
    
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        provider_choice = st.selectbox(
            "Select AI Provider",
            options=list(configured_providers.keys()),
            format_func=lambda x: configured_providers[x]["name"]
        )
    
    with col2:
        # Model selection based on provider
        available_models = configured_providers[provider_choice]["models"]
        
        # Model display names and cost info
        model_info = {
            # OpenAI GPT-5 models (LATEST!)
            "gpt-5.1": {"name": "GPT-5.1 (Latest - Best for Coding)", "cost": "$1.00-2.00 CAD"},
            "gpt-5-pro": {"name": "GPT-5 Pro (Smarter & More Precise)", "cost": "$1.50-3.00 CAD"},
            "gpt-5": {"name": "GPT-5 (Intelligent Reasoning)", "cost": "$1.00-2.00 CAD"},
            "gpt-5-mini": {"name": "GPT-5 Mini (Cost-Efficient)", "cost": "$0.20-0.40 CAD"},
            "gpt-5-nano": {"name": "GPT-5 Nano (Fastest)", "cost": "$0.10-0.20 CAD"},
            "gpt-4.1": {"name": "GPT-4.1 (Smartest Non-Reasoning)", "cost": "$0.80-1.50 CAD"},
            # OpenAI GPT-4 models
            "gpt-4o": {"name": "GPT-4o", "cost": "$0.50-1.00 CAD"},
            "gpt-4o-mini": {"name": "GPT-4o Mini", "cost": "$0.05-0.10 CAD"},
            "gpt-4-turbo": {"name": "GPT-4 Turbo", "cost": "$2.00-3.50 CAD"},
            "gpt-4": {"name": "GPT-4", "cost": "$6.00-8.00 CAD"},
            "gpt-3.5-turbo": {"name": "GPT-3.5 Turbo (Legacy)", "cost": "$0.10-0.20 CAD"},
            # Anthropic Claude 4.x models
            "claude-opus-4-5": {"name": "Claude Opus 4.5 (Premium)", "cost": "$2.00-4.00 CAD"},
            "claude-opus-4-5-20251101": {"name": "Claude Opus 4.5 (Nov 2025)", "cost": "$2.00-4.00 CAD"},
            "claude-sonnet-4-5": {"name": "Claude Sonnet 4.5 (Best Value)", "cost": "$0.40-1.00 CAD"},
            "claude-haiku-4-5": {"name": "Claude Haiku 4.5 (Fastest)", "cost": "$0.10-0.30 CAD"},
            "claude-3-7-sonnet-latest": {"name": "Claude 3.7 Sonnet (Extended Thinking)", "cost": "$0.40-1.00 CAD"},
            "claude-3-7-sonnet-20250219": {"name": "Claude 3.7 Sonnet (Feb 2025)", "cost": "$0.40-1.00 CAD"},
            "claude-3-5-haiku-latest": {"name": "Claude 3.5 Haiku", "cost": "$0.10-0.30 CAD"},
            "claude-3-5-sonnet-20241022": {"name": "Claude 3.5 Sonnet (Oct 2024)", "cost": "$0.30-0.80 CAD"},
            "claude-3-opus-20240229": {"name": "Claude 3 Opus (Legacy)", "cost": "$1.50-3.00 CAD"},
            # Google Gemini 3.x models (LATEST!)
            "gemini-3-pro": {"name": "Gemini 3 Pro (Most Intelligent)", "cost": "$0.50-1.00 CAD"},
            # Google Gemini 2.x models
            "gemini-2.5-pro": {"name": "Gemini 2.5 Pro (Advanced Thinking)", "cost": "$0.30-0.70 CAD"},
            "gemini-2.5-flash": {"name": "Gemini 2.5 Flash (Best Price/Performance)", "cost": "$0.15-0.35 CAD"},
            "gemini-2.5-flash-lite": {"name": "Gemini 2.5 Flash-Lite (Ultra Fast)", "cost": "$0.10-0.25 CAD"},
            "gemini-2.0-flash": {"name": "Gemini 2.0 Flash", "cost": "$0.10-0.30 CAD"},
            "gemini-2.0-flash-exp": {"name": "Gemini 2.0 Flash Experimental", "cost": "$0.10-0.30 CAD"},
            "gemini-2.0-flash-lite": {"name": "Gemini 2.0 Flash-Lite", "cost": "$0.08-0.20 CAD"},
            # Google Gemini 1.x models
            "gemini-1.5-pro": {"name": "Gemini 1.5 Pro", "cost": "$0.20-0.50 CAD"},
            "gemini-1.5-flash": {"name": "Gemini 1.5 Flash", "cost": "$0.05-0.15 CAD"},
            "gemini-1.5-flash-8b": {"name": "Gemini 1.5 Flash-8B", "cost": "$0.04-0.12 CAD"},
            "gemini-1.5-pro-latest": {"name": "Gemini 1.5 Pro Latest", "cost": "$0.20-0.50 CAD"},
        }
        
        model_choice = st.selectbox(
            "Select Model",
            options=available_models,
            format_func=lambda x: f"{model_info.get(x, {}).get('name', x)}",
            help="Different models have different costs and capabilities"
        )
        
        # Show cost estimate
        if model_choice in model_info:
            st.caption(f"💰 Est. cost: {model_info[model_choice]['cost']} per analysis")
    
    with col3:
        # Optional: Competitor Intelligence
        use_intelligence = st.checkbox(
            "Include Competitor Intel",
            value=False,
            help="Scrape web for competitor and market data (slower)"
        )
    
    # Analyze button
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        analyze_button = st.button("⚔️ ANALYZE", type="primary", use_container_width=True)
    
    with col2:
        if st.button("🔄 Clear", use_container_width=True):
            st.session_state.business_data = {}
            st.session_state.current_analysis = None
            st.rerun()
    
    # Run analysis
    if analyze_button:
        if not business_data.get("description"):
            st.error("Please provide at least a business description.")
            return
        
        run_analysis(business_data, provider_choice, model_choice, use_intelligence)
    
    # Show results if available
    if st.session_state.current_analysis:
        st.markdown("---")
        st.markdown("## 📋 Analysis Results")
        
        result, business_data, provider_used, usage_info = st.session_state.current_analysis
        
        # Show usage info for this analysis
        if usage_info:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Tokens Used", f"{usage_info['input_tokens'] + usage_info['output_tokens']:,}")
            with col2:
                st.metric("Input Tokens", f"{usage_info['input_tokens']:,}")
            with col3:
                st.metric("Output Tokens", f"{usage_info['output_tokens']:,}")
            with col4:
                st.metric("Cost (CAD)", f"${usage_info['cost_cad']:.4f}")
        
        # Save to history button
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("💾 Save to History", use_container_width=True):
                save_analysis_to_history(business_data, result, provider_used)
                st.success("✅ Saved to history!")
        
        with col2:
            # Export options
            export_format = st.selectbox("Export", ["None", "Markdown", "Text"], key="export")
            if export_format == "Markdown":
                markdown_report = generate_markdown_report(result, business_data)
                st.download_button(
                    "📥 Download Markdown",
                    data=markdown_report,
                    file_name=f"analysis_{business_data.get('name', 'report')}.md",
                    mime="text/markdown"
                )
        
        st.markdown("---")
        
        # Render the analysis with competitor data
        render_full_analysis(result, st.session_state.competitor_data)


def show_structured_form():
    """Show structured business input form."""
    
    col1, col2 = st.columns(2)
    
    with col1:
        business_name = st.text_input(
            "Business Name / Concept *",
            value=st.session_state.business_data.get("name", ""),
            help="The name or core concept of your business"
        )
        
        target_market = st.text_area(
            "Target Market *",
            value=st.session_state.business_data.get("target_market", ""),
            height=100,
            help="Who are your customers? Be specific."
        )
        
        revenue_model = st.text_area(
            "Revenue Model *",
            value=st.session_state.business_data.get("revenue_model", ""),
            height=100,
            help="How will you make money?"
        )
    
    with col2:
        assumptions = st.text_area(
            "Key Assumptions",
            value=st.session_state.business_data.get("assumptions", ""),
            height=100,
            help="What are you assuming will be true?"
        )
        
        competitive_landscape = st.text_area(
            "Competitive Landscape",
            value=st.session_state.business_data.get("competitive_landscape", ""),
            height=100,
            help="Who are your competitors? What's your advantage?"
        )
    
    description = st.text_area(
        "Detailed Description *",
        value=st.session_state.business_data.get("description", ""),
        height=200,
        help="Provide a comprehensive description of your business idea, including the problem you're solving, your solution, and your go-to-market strategy."
    )
    
    return {
        "name": business_name,
        "description": description,
        "target_market": target_market,
        "revenue_model": revenue_model,
        "assumptions": assumptions,
        "competitive_landscape": competitive_landscape
    }


def show_quick_form():
    """Show quick analysis form."""
    
    st.markdown("""
    <div class="info-box">
        <strong>Quick Analysis Mode</strong><br>
        Just paste your business idea or pitch and get instant feedback.
    </div>
    """, unsafe_allow_html=True)
    
    description = st.text_area(
        "Business Idea / Pitch",
        value=st.session_state.business_data.get("description", ""),
        height=300,
        help="Describe your business idea in as much detail as possible"
    )
    
    return {
        "name": "Quick Analysis",
        "description": description,
        "target_market": "Not specified",
        "revenue_model": "Not specified",
        "assumptions": "None provided",
        "competitive_landscape": "Not specified"
    }


def show_upload_form():
    """Show document upload form."""
    
    st.markdown("""
    <div class="info-box">
        <strong>Document Upload</strong><br>
        Upload your business plan or pitch deck (PDF, DOCX, TXT)
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "docx", "txt"],
        help="Upload your business plan document"
    )
    
    description = ""
    
    if uploaded_file:
        try:
            if uploaded_file.type == "text/plain":
                description = uploaded_file.read().decode("utf-8")
            elif uploaded_file.type == "application/pdf":
                from PyPDF2 import PdfReader
                pdf = PdfReader(uploaded_file)
                description = "\n".join([page.extract_text() for page in pdf.pages])
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                from docx import Document
                doc = Document(uploaded_file)
                description = "\n".join([para.text for para in doc.paragraphs])
            
            st.success(f"✅ Document loaded: {len(description)} characters")
        except Exception as e:
            st.error(f"Error reading document: {str(e)}")
    
    # Allow editing
    description = st.text_area(
        "Extracted / Edit Content",
        value=description,
        height=300
    )
    
    business_name = st.text_input("Business Name (optional)")
    
    return {
        "name": business_name or "Uploaded Document Analysis",
        "description": description,
        "target_market": "See document",
        "revenue_model": "See document",
        "assumptions": "See document",
        "competitive_landscape": "See document"
    }


def run_analysis(business_data: dict, provider_name: str, model_name: str, use_intelligence: bool):
    """Run the business analysis."""
    
    with st.spinner(""):
        render_loading_message()
        
        try:
            # Gather intelligence if requested
            competitor_intel = None
            competitor_data = {"enabled": use_intelligence, "sources": []}
            
            if use_intelligence:
                st.info("🔍 Gathering competitor intelligence...")
                researcher = MarketResearcher()
                research = researcher.research_market(business_data)
                competitor_intel = researcher.format_research_for_analysis(research)
                
                # Store the raw intelligence data for display
                if research.get("competitor_intelligence"):
                    intel = research["competitor_intelligence"]
                    competitor_data = {
                        "enabled": True,
                        "sources": intel.get("sources", []),
                        "error": intel.get("error")  # Include error message if present
                    }
            
            # Create auditor with specified model and analyze
            auditor = Auditor(provider_name=provider_name, model=model_name)
            result, usage_info = auditor.analyze(business_data, competitor_intel)
            
            # Store in session state with usage info and competitor data
            st.session_state.current_analysis = (result, business_data, provider_name, usage_info)
            st.session_state.business_data = business_data
            st.session_state.last_usage = usage_info
            st.session_state.competitor_data = competitor_data
            
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Analysis failed: {str(e)}")
            st.code(traceback.format_exc())


def save_analysis_to_history(business_data: dict, result, provider_name: str):
    """Save analysis to history database."""
    try:
        repo.save_analysis(business_data, result, provider_name)
    except Exception as e:
        st.error(f"Failed to save: {str(e)}")


def show_previous_analysis():
    """Show a previously saved analysis."""
    
    analysis = repo.get_analysis_by_id(st.session_state.selected_history_id)
    
    if not analysis:
        st.error("Analysis not found")
        st.session_state.selected_history_id = None
        return
    
    # Back button
    if st.button("← Back to New Analysis"):
        st.session_state.selected_history_id = None
        st.rerun()
    
    st.markdown(f"## 📋 Saved Analysis: {analysis.business_name}")
    st.caption(f"Analyzed on {analysis.timestamp.strftime('%Y-%m-%d %H:%M')}" if analysis.timestamp else "")
    st.caption(f"Provider: {analysis.ai_provider_used}")
    
    st.markdown("---")
    
    # Show full analysis as HTML
    st.markdown(analysis.full_analysis)


def show_history_page():
    """Show analysis history page."""
    
    st.markdown("## 📚 Analysis History")
    
    # Statistics
    stats = repo.get_statistics()
    render_statistics(stats)
    
    st.markdown("---")
    
    # Filters
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search_query = st.text_input("🔍 Search", placeholder="Search by name or description...")
    
    with col2:
        filter_verdict = st.selectbox("Filter by Verdict", ["All", "VIABLE", "RISKY", "DEAD ON ARRIVAL"])
    
    with col3:
        st.write("")  # Spacing
    
    # Get analyses
    if search_query:
        analyses = repo.search_analyses(search_query)
    elif filter_verdict != "All":
        analyses = repo.filter_by_verdict(filter_verdict)
    else:
        analyses = repo.get_all_analyses(limit=50)
    
    st.markdown(f"### {len(analyses)} Analysis Results")
    
    if not analyses:
        st.info("No analyses found. Run your first analysis to get started!")
        return
    
    # Display analyses
    for analysis in analyses:
        with st.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                verdict_emoji = {"VIABLE": "✅", "RISKY": "⚠️", "DEAD ON ARRIVAL": "❌"}.get(analysis.verdict, "❓")
                st.markdown(f"**{verdict_emoji} {analysis.business_name}**")
                st.caption(analysis.idea_description[:150] + "..." if len(analysis.idea_description) > 150 else analysis.idea_description)
            
            with col2:
                st.caption(analysis.timestamp.strftime("%Y-%m-%d") if analysis.timestamp else "N/A")
            
            with col3:
                if st.button("View", key=f"view_{analysis.id}"):
                    st.session_state.selected_history_id = analysis.id
                    st.switch_page("main.py")
            
            with col4:
                if st.button("Delete", key=f"del_{analysis.id}"):
                    if repo.delete_analysis(analysis.id):
                        st.success("Deleted!")
                        st.rerun()
        
        st.markdown("---")


def show_usage_page():
    """Show API usage and cost tracking page."""
    
    st.markdown("## 💰 API Usage & Cost Tracking")
    
    # Time period selector
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("Track your AI API usage and costs in Canadian Dollars (CAD)")
    
    with col2:
        period = st.selectbox("Period", ["All Time", "Last 7 Days", "Last 30 Days", "Today"])
    
    # Map period to days
    period_days = {
        "All Time": None,
        "Last 7 Days": 7,
        "Last 30 Days": 30,
        "Today": 1
    }
    
    # Get usage statistics
    stats = get_usage_stats(days=period_days[period])
    
    st.markdown("---")
    
    # Show alert if costs are high
    if stats['total_cost_cad'] >= 10.0:
        render_usage_alert(stats['total_cost_cad'], threshold=10.0)
    
    # Main usage dashboard
    render_usage_dashboard(stats)
    
    st.markdown("---")
    
    # Recent usage table
    recent = get_recent_usage(limit=20)
    render_recent_usage_table(recent)
    
    st.markdown("---")
    
    # Cost estimator
    render_cost_estimator()
    
    st.markdown("---")
    
    # Additional info
    with st.expander("ℹ️ About Cost Tracking"):
        st.markdown("""
        ### How Costs Are Calculated
        
        Costs are calculated based on:
        - **Input tokens**: Text sent to the AI (your prompts)
        - **Output tokens**: Text generated by the AI (the analysis)
        - **Provider pricing**: Each AI provider has different rates
        - **Exchange rate**: USD to CAD conversion (currently 1.36)
        
        ### Pricing (per 1M tokens)
        
        **OpenAI GPT-4o:**
        - Input: $2.50 USD / Output: $10.00 USD
        - Average analysis: ~$0.50-1.00 CAD
        
        **Anthropic Claude 3.5 Sonnet:**
        - Input: $3.00 USD / Output: $15.00 USD
        - Average analysis: ~$0.30-0.80 CAD
        
        **Google Gemini 1.5 Pro:**
        - Input: $1.25 USD / Output: $5.00 USD
        - Average analysis: ~$0.20-0.50 CAD (often free tier)
        
        ### Tips to Reduce Costs
        
        1. Use **Google Gemini** for the cheapest option
        2. Use **Quick Analysis** mode instead of uploading long documents
        3. Disable **Competitor Intelligence** when not needed
        4. Compare providers - some are 50% cheaper for similar quality
        
        ### Data Storage
        
        Usage data is stored locally in your SQLite database and never shared externally.
        """)


def show_settings_page():
    """Show settings and configuration page."""
    
    st.markdown("## ⚙️ Settings & Configuration")
    
    st.markdown("### 🔑 API Keys")
    
    st.markdown("""
    <div class="info-box">
        <strong>API keys are configured via the .env file.</strong><br>
        For security reasons, API keys must be set in your environment, not in the UI.
    </div>
    """, unsafe_allow_html=True)
    
    # Show which providers are configured
    providers = get_available_providers()
    
    st.markdown("#### Current Configuration")
    
    for provider_key, provider_info in providers.items():
        status = "✅ Configured" if provider_info['configured'] else "❌ Not Configured"
        color = "#10b981" if provider_info['configured'] else "#ef4444"
        
        st.markdown(f"""
        <div style="padding: 0.5rem; margin: 0.5rem 0; background-color: #1e293b; border-left: 3px solid {color}; border-radius: 4px;">
            <strong>{provider_info['name']}</strong>: {status}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("#### How to Add API Keys")
    
    st.markdown("""
    1. **Create/Edit your `.env` file** in the project root directory
    2. **Add your API keys** (see `.env.example` for template)
    3. **Restart the application** to load the new keys
    
    **Example `.env` file:**
    ```
    OPENAI_API_KEY=sk-proj-your_key_here
    ANTHROPIC_API_KEY=sk-ant-your_key_here
    GOOGLE_API_KEY=your_key_here
    SERPER_API_KEY=your_key_here
    ```
    
    **Need help?**
    - See [SETUP.md](https://github.com/your-repo/blob/main/SETUP.md) for detailed instructions
    - See [API_KEYS_GUIDE.md](https://github.com/your-repo/blob/main/API_KEYS_GUIDE.md) for provider-specific guides
    - See [SECURITY.md](https://github.com/your-repo/blob/main/SECURITY.md) for security best practices
    """)
    
    st.markdown("---")
    
    st.markdown("### 🌐 Web Scraping")
    
    scraping_enabled = st.checkbox(
        "Enable Competitor Intelligence Scraping",
        value=config.SCRAPING_ENABLED,
        help="Enable web scraping to gather competitor and market data"
    )
    
    st.markdown("---")
    
    st.markdown("### ℹ️ About")
    
    st.markdown("""
    **The Devil's Advocate** is a red team business analysis tool that ruthlessly 
    evaluates business ideas using a Pre-Mortem framework.
    
    **Version:** 1.1.0
    
    **Features:**
    - Multi-AI provider support (OpenAI, Anthropic, Google)
    - Pre-Mortem analysis framework
    - Competitor intelligence gathering
    - Analysis history and search
    - API usage and cost tracking (NEW!)
    - Export to Markdown
    
    **Created by:** The Devil's Advocate Team
    """)


if __name__ == "__main__":
    main()

