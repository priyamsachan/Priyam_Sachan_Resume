import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Priyam Sachan | Senior Data Engineer Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Refined Professional CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at top left, #0f172a, #1e293b);
        color: #f1f5f9;
    }

    /* Glassmorphism Card Style */
    .res-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    
    .res-card:hover {
        border-color: #38bdf8;
        background: rgba(56, 189, 248, 0.04);
        transform: translateY(-2px);
    }

    /* Skill Badge Styling */
    .skill-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 6px;
        background: rgba(14, 165, 233, 0.15);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        margin: 3px;
        font-size: 13px;
        font-weight: 500;
    }

    /* Header Gradients */
    h1, h2 {
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    .job-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
    }
    
    .exp-date {
        color: #94a3b8;
        font-weight: 600;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR
