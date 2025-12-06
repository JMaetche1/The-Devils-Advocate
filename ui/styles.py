"""Custom CSS styling for The Devil's Advocate UI."""


def get_custom_css() -> str:
    """Return custom CSS for the application."""
    return """
    <style>
    /* Main app styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .app-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1e3a8a 0%, #991b1b 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .app-header h1 {
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
    }
    
    .app-header p {
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Verdict styling */
    .verdict-viable {
        background-color: #10b981;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
    }
    
    .verdict-risky {
        background-color: #f59e0b;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
    }
    
    .verdict-doa {
        background-color: #ef4444;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Kill Shot styling */
    .kill-shot {
        background-color: #7f1d1d;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #dc2626;
        margin: 1.5rem 0;
    }
    
    .kill-shot h3 {
        margin-top: 0;
        color: #fca5a5;
    }
    
    /* Scenario cards */
    .scenario-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #3b82f6;
    }
    
    .scenario-card h4 {
        color: #60a5fa;
        margin-top: 0;
    }
    
    /* Steel Man styling */
    .steel-man {
        background-color: #064e3b;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #10b981;
        margin: 1.5rem 0;
    }
    
    .steel-man h3 {
        margin-top: 0;
        color: #6ee7b7;
    }
    
    /* History item */
    .history-item {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #374151;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .history-item:hover {
        background-color: #1f2937;
        border-color: #3b82f6;
    }
    
    /* Stats */
    .stat-box {
        text-align: center;
        padding: 1rem;
        border-radius: 8px;
        background-color: #1e293b;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #60a5fa;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-top: 0.5rem;
    }
    
    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    /* File uploader */
    .uploadedFile {
        border-radius: 8px;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    /* Loading animation */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .loading {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    /* Info box */
    .info-box {
        background-color: #1e3a8a;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Warning box */
    .warning-box {
        background-color: #92400e;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    </style>
    """


def get_verdict_class(verdict: str) -> str:
    """Get CSS class for verdict."""
    verdict_upper = verdict.upper()
    
    if verdict_upper == "VIABLE":
        return "verdict-viable"
    elif verdict_upper == "RISKY":
        return "verdict-risky"
    elif verdict_upper == "DEAD ON ARRIVAL":
        return "verdict-doa"
    else:
        return "verdict-risky"  # Default


