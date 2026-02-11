import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Priyam Sachan | Senior Data Engineer",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Framer-Inspired UI Styling (Minimalist Bento Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    :root {
        --primary-color: #ffffff;
        --secondary-color: #888888;
        --bg-dark: #000000;
        --card-bg: #111111;
        --border-color: #222222;
    }

    /* Background and Global Styles */
    .stApp {
        background-color: var(--bg-dark);
        color: var(--primary-color);
        font-family: 'Inter', sans-serif;
    }

    /* Bento Grid Cards */
    .bento-card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        padding: 2rem;
        border-radius: 24px;
        margin-bottom: 20px;
        transition: border 0.3s ease;
    }
    
    .bento-card:hover {
        border-color: #444444;
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 8px;
        background: #1a1a1a;
        color: #eeeeee;
        border: 1px solid #333333;
        margin: 4px;
        font-size: 12px;
        font-weight: 500;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Large Minimalist Typography */
    h1 {
        font-weight: 700;
        font-size: 4rem !important;
        letter-spacing: -2px !important;
        margin-bottom: 0px !important;
        color: white !important;
    }

    h2 {
        font-weight: 600;
        font-size: 2rem !important;
        letter-spacing: -1px !important;
        color: #ffffff !important;
        margin-top: 2rem !important;
    }

    .subtitle {
        color: var(--secondary-color);
        font-size: 1.5rem;
        margin-bottom: 3rem;
    }

    .job-title { font-weight: 600; font-size: 1.4rem; color: #fff; }
    .company-name { color: var(--secondary-color); font-weight: 400; font-size: 1rem; }
    .date-tag { font-family: 'JetBrains Mono', monospace; color: #555555; font-size: 0.8rem; text-transform: uppercase; }
    
    /* Custom Sidebar for Minimalist look */
    [data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #111;
    }
    
    /* Buttons */
    .stButton>button {
        border-radius: 12px;
        background-color: white;
        color: black;
        border: none;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<h1>Priyam Sachan</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Senior Data Engineer</p>", unsafe_allow_html=True)

col_bio, col_contact = st.columns([2, 1])

with col_bio:
    st.markdown("""
    Expert in architecting end-to-end data ecosystems. I specialize in cloud migrations, 
    Medallion Data Lakehouses, and high-performance ETL/ELT orchestration.
    """)

with col_contact:
    st.write("📞 [+91 8840750905](tel:+918840750905)")
    st.write("📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan)")

# --- SKILL GRID (Bento Layout) ---
st.markdown("<h2>Technical Arsenal</h2>", unsafe_allow_html=True)
def render_tags(items):
    return "".join([f'<span class="skill-tag">{s}</span>' for s in items])

s1, s2, s3 = st.columns(3)
with s1:
    st.markdown(f"""<div class="bento-card">
    <p style='color:#888; font-size:0.8rem; font-weight:600; text-transform:uppercase;'>Engineering</p>
    {render_tags(["Python", "SQL", "PySpark", "Spark", "Scala", "Pandas"])}
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown(f"""<div class="bento-card">
    <p style='color:#888; font-size:0.8rem; font-weight:600; text-transform:uppercase;'>Cloud & Infrastructure</p>
    {render_tags(["AWS S3", "Azure Synapse", "Databricks", "Snowflake", "MS Fabric", "ADF"])}
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown(f"""<div class="bento-card">
    <p style='color:#888; font-size:0.8rem; font-weight:600; text-transform:uppercase;'>Analytics & AI</p>
    {render_tags(["Power BI", "DAX", "Git", "Postman", "Generative AI", "Copilot"])}
    </div>""", unsafe_allow_html=True)

# --- PROFESSIONAL JOURNEY ---
st.markdown("<h2>Experience</h2>", unsafe_allow_html=True)

# Mastercard
st.markdown(f"""
<div class="bento-card">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
        <span class="job-title">Senior Data Engineer</span>
        <span class="date-tag">JAN 2025 — PRESENT</span>
    </div>
    <div class="company-name">Mastercard, Pune</div>
    <br>
    <ul style="color: #aaa; font-size: 0.95rem; line-height: 1.6;">
        <li><b>Cloud Migration:</b> Architected complete migration from on-prem Oracle to AWS Cloud.</li>
        <li><b>Orchestration:</b> Deployed incremental ETL using Apache Nifi for unified transaction event ingestion.</li>
        <li><b>Data Processing:</b> Developed Python/Scala Databricks notebooks for Parquet optimization in S3 (Bronze).</li>
        <li><b>Architecture:</b> Established Medallion Data Architecture (Bronze/Silver/Gold) to ensure high data quality.</li>
        <li><b>Modeling:</b> Constructed Canonical Data Models (CDM) in the Gold layer for analytical reporting.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# EY
st.markdown(f"""
<div class="bento-card">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
        <span class="job-title">Data Engineer</span>
        <span class="date-tag">NOV 2023 — JAN 2025</span>
    </div>
    <div class="company-name">Ernst & Young, Pune</div>
    <br>
    <ul style="color: #aaa; font-size: 0.95rem; line-height: 1.6;">
        <li><b>Data Warehousing:</b> Implemented Snowflake solutions for structured and semi-structured formats.</li>
        <li><b>Automation:</b> Developed high-efficiency pipelines using Snowpipe and External Integration.</li>
        <li><b>Transformation:</b> Authored advanced SQL for schema creation and metadata management.</li>
        <li><b>Supply Chain:</b> Delivered Power BI reporting for tracking key US FMCG client metrics.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# TCS
st.markdown(f"""
<div class="bento-card">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
        <span class="job-title">Data Engineer</span>
        <span class="date-tag">NOV 2020 — OCT 2023</span>
    </div>
    <div class="company-name">Tata Consultancy Services, Pune</div>
    <br>
    <ul style="color: #aaa; font-size: 0.95rem; line-height: 1.6;">
        <li><b>ERP Migration:</b> Deployed ADF CDC pipelines for SAP migration, reducing cycle time by 30%.</li>
        <li><b>FinOps:</b> Created Analytics Dashboards using Azure Monitor APIs for cost governance.</li>
        <li><b>Optimization:</b> Enhanced Synapse workflows with PySpark/SQL for compliance operations.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- EDUCATION & CERTIFICATIONS ---
st.markdown("<h2>Education & Honors</h2>", unsafe_allow_html=True)
c1, c2 = st.columns(2)

with c1:
    st.markdown(f"""
    <div class="bento-card">
        <p style='color:#888; font-size:0.8rem; font-weight:600; text-transform:uppercase;'>Education</p>
        <p style='margin-bottom:4px;'><b>B.Tech in Mechanical Engineering</b></p>
        <p class="company-name">Medi-caps University (2016-2020) | CGPA: 7.95</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="bento-card">
        <p style='color:#888; font-size:0.8rem; font-weight:600; text-transform:uppercase;'>Certifications</p>
        <div style="font-size: 0.9rem; color: #aaa;">
            Snow Pro Core • Databricks Associate • MS Fabric (DP-700) • Power BI (PL-300) • Azure Data Eng (DP-203)
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><center style='opacity:0.3; font-size:0.8rem;'>Built with ❤️ • 2026 Portfolio</center>", unsafe_allow_html=True)
