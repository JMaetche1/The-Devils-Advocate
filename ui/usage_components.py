"""UI components for displaying API usage statistics."""

import streamlit as st
from typing import Dict
from datetime import datetime


def render_usage_dashboard(stats: Dict):
    """Render the complete usage dashboard."""
    
    st.markdown("### 💰 API Usage & Costs")
    
    # Total usage metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total API Calls",
            f"{stats['total_calls']:,}",
            help="Total number of AI API calls made"
        )
    
    with col2:
        st.metric(
            "Total Tokens",
            f"{stats['total_tokens']:,}",
            help="Combined input and output tokens"
        )
    
    with col3:
        st.metric(
            "Cost (USD)",
            f"${stats['total_cost_usd']:.4f}",
            help="Total cost in US Dollars"
        )
    
    with col4:
        st.metric(
            "Cost (CAD)",
            f"${stats['total_cost_cad']:.2f}",
            help="Total cost in Canadian Dollars",
            delta=None
        )
    
    st.markdown("---")
    
    # Breakdown by provider
    if stats['by_provider']:
        st.markdown("#### 📊 Breakdown by AI Provider")
        
        provider_names = {
            'openai': '🟢 OpenAI',
            'anthropic': '🔵 Anthropic',
            'google': '🟡 Google'
        }
        
        for provider, data in stats['by_provider'].items():
            with st.expander(f"{provider_names.get(provider, provider)} - ${data['cost_cad']:.2f} CAD"):
                pcol1, pcol2, pcol3 = st.columns(3)
                
                with pcol1:
                    st.metric("Calls", f"{data['calls']:,}")
                
                with pcol2:
                    st.metric("Tokens", f"{data['tokens']:,}")
                
                with pcol3:
                    st.metric("Cost (CAD)", f"${data['cost_cad']:.2f}")


def render_usage_summary_card(stats: Dict):
    """Render a compact usage summary card."""
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #1e3a8a 0%, #312e81 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    ">
        <h4 style="margin: 0 0 1rem 0; color: #60a5fa;">💰 Current Session Costs</h4>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">Total API Calls</p>
                <p style="margin: 0; font-size: 1.5rem; font-weight: bold;">{stats['total_calls']}</p>
            </div>
            <div>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">Total Cost</p>
                <p style="margin: 0; font-size: 1.5rem; font-weight: bold;">${stats['total_cost_cad']:.2f} CAD</p>
            </div>
            <div>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">Avg per Call</p>
                <p style="margin: 0; font-size: 1.5rem; font-weight: bold;">
                    ${(stats['total_cost_cad'] / stats['total_calls'] if stats['total_calls'] > 0 else 0):.2f}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_recent_usage_table(recent_records):
    """Render a table of recent API usage."""
    
    st.markdown("#### 📝 Recent API Calls")
    
    if not recent_records:
        st.info("No usage records yet. Run your first analysis!")
        return
    
    # Create table data
    table_data = []
    for record in recent_records:
        table_data.append({
            "Time": record.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "Provider": record.provider.title(),
            "Model": record.model,
            "Tokens": f"{record.total_tokens:,}",
            "Cost (CAD)": f"${record.cost_cad:.4f}"
        })
    
    st.table(table_data)


def render_cost_breakdown_chart(stats: Dict):
    """Render a pie chart of costs by provider."""
    
    if not stats['by_provider']:
        return
    
    st.markdown("#### 📈 Cost Distribution")
    
    # Prepare data for chart
    providers = []
    costs = []
    
    for provider, data in stats['by_provider'].items():
        providers.append(provider.title())
        costs.append(data['cost_cad'])
    
    # Create simple bar chart using Streamlit
    chart_data = {
        'Provider': providers,
        'Cost (CAD)': costs
    }
    
    st.bar_chart(data=chart_data, x='Provider', y='Cost (CAD)')


def render_usage_alert(current_cost_cad: float, threshold: float = 10.0):
    """Show an alert if costs exceed threshold."""
    
    if current_cost_cad >= threshold:
        st.warning(f"""
        ⚠️ **Cost Alert**: Your API usage has reached **${current_cost_cad:.2f} CAD**.
        
        Consider:
        - Using Google Gemini (cheapest option)
        - Reducing analysis frequency
        - Checking your budget settings
        """)


def render_cost_estimator():
    """Render a cost estimator tool."""
    
    st.markdown("#### 💵 Cost Estimator")
    
    st.caption("Estimate costs before running analyses")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_analyses = st.number_input(
            "Number of analyses",
            min_value=1,
            max_value=1000,
            value=10,
            step=1
        )
    
    with col2:
        provider_choice = st.selectbox(
            "AI Provider",
            ["OpenAI (GPT-4o)", "Anthropic (Claude 3.5)", "Google (Gemini 1.5)"]
        )
    
    # Estimate costs
    avg_costs = {
        "OpenAI (GPT-4o)": 0.75,
        "Anthropic (Claude 3.5)": 0.55,
        "Google (Gemini 1.5)": 0.35
    }
    
    avg_cost_cad = avg_costs[provider_choice]
    total_cost_cad = avg_cost_cad * num_analyses
    
    st.info(f"""
    **Estimated Cost**: ${total_cost_cad:.2f} CAD
    
    - Average per analysis: ${avg_cost_cad:.2f} CAD
    - Total for {num_analyses} analyses: ${total_cost_cad:.2f} CAD
    
    *Note: Actual costs may vary based on input length and analysis complexity.*
    """)


def render_usage_export_button(stats: Dict):
    """Render a button to export usage data."""
    
    import json
    from datetime import datetime
    
    if st.button("📥 Export Usage Data"):
        export_data = {
            "exported_at": datetime.now().isoformat(),
            "total_statistics": stats,
        }
        
        json_str = json.dumps(export_data, indent=2)
        
        st.download_button(
            "Download JSON",
            data=json_str,
            file_name=f"api_usage_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )


