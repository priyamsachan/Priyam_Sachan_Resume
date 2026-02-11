import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Priyam Sachan | Senior Data Engineer",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium UI Styling (Midnight Aurora Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    :root {
        --primary: #00f2fe;
        --secondary: #4facfe;
        --bg-dark: #0b0f19;
        --card-bg: rgba(23, 32, 53, 0.7);
    }

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at 20% 10%, #1e293b 0%, #0f172a 100%);
        color: #e2e8f0;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .glass-card:hover {
        border-color: var(--primary);
        transform: scale(1.01);
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.15);
    }

    /* Modern Skill Badges */
    .skill-chip {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 50px;
        background: linear-gradient(90deg, rgba(79, 172, 254, 0.1), rgba(0, 242, 254, 0.1));
        color: var(--primary);
        border: 1px solid rgba(0, 242, 254, 0.3);
        margin: 5px;
        font-size: 13px;
        font-weight: 500;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Typography Upgrades */
    h1, h2 {
        background: linear-gradient(120deg, #fff 30%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
    }

    .job-title { color: var(--primary); font-weight: 700; font-size: 1.4rem; margin-bottom: 2px; }
    .company-name { color: #94a3b8; font-weight: 500; font-size: 1.1rem; }
    .date-tag { font-family: 'JetBrains Mono', monospace; color: #64748b; font-size: 0.9rem; }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0b0f19;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=120)
    st.title("Priyam Sachan")
    st.write("📞 [+91 8840750905](tel:+918840750905)")
    st.write("📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")
    st.write("🔗 [LinkedIn Profile](https://linkedin.com/in/priyam-sachan)")
    
    st.divider()
    st.write("## 💡 Leadership")
    st.markdown("""
    Strategic Thinking • Mentorship • Technical Collaboration
    """)
    
    st.divider()
    st.download_button("📂 Get Official Resume", "PDF_DATA", file_name="Priyam_Sachan_Resume.pdf", use_container_width=True)

# --- HERO SECTION ---
st.title("Senior Data Engineer")
st.write("### Building the backbone of modern data intelligence.")
st.markdown("""
Expert in architecting end-to-end data ecosystems. I specialize in cloud migrations, 
Medallion Data Lakehouses, and high-performance ETL/ELT orchestration.
""")

# --- SKILL GRID ---
st.write("## ⚡ Technical Arsenal")
def render_chips(list):
    return "".join([f'<span class="skill-chip">{s}</span>' for s in list])

s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("#### 🛠️ Core Engineering")
    st.markdown(render_chips(["Python", "SQL", "PySpark", "Spark", "Scala", "Pandas", "NumPy"]), unsafe_allow_html=True)
with s2:
    st.markdown("#### ☁️ Cloud & Big Data")
    st.markdown(render_chips(["AWS S3", "Azure Synapse", "Databricks", "Snowflake", "MS Fabric", "Nifi", "ADF"]), unsafe_allow_html=True)
with s3:
    st.markdown("#### 📈 Analytics & AI")
    st.markdown(render_chips(["Power BI", "DAX", "Data Modeling", "Git", "Postman", "Generative AI", "Copilot"]), unsafe_allow_html=True)

st.divider()

# --- PROFESSIONAL JOURNEY ---
st.write("## 💼 Professional Journey")

# Mastercard
st.markdown(f"""
<div class="glass-card">
    <div class="job-title">Senior Data Engineer</div>
    <div class="company-name">Mastercard, Pune</div>
    <div class="date-tag">JAN 2025 — PRESENT</div>
    <br>
    <ul>
        <li><b>Cloud Migration:</b> Architected complete migration from on-prem Oracle to AWS Cloud[cite: 15].</li>
        <li><b>Orchestration:</b> Deployed incremental ETL using Apache Nifi for unified transaction event ingestion[cite: 16].</li>
        <li><b>Data Processing:</b> Developed Python/Scala Databricks notebooks for Parquet optimization in S3 (Bronze)[cite: 17, 21].</li>
        <li><b>Architecture:</b> Established Medallion Data Architecture (Bronze/Silver/Gold) to ensure high data quality[cite: 18, 19].</li>
        <li><b>Modeling:</b> Constructed Canonical Data Models (CDM) in the Gold layer for Fact/Dimension analytical reporting[cite: 20].</li>
    </ul>
</div>
""", unsafe_allow_html=True)



# EY
st.markdown(f"""
<div class="glass-card">
    <div class="job-title">Data Engineer</div>
    <div class="company-name">Ernst & Young, Pune</div>
    <div class="date-tag">NOV 2023 — JAN 2025</div>
    <br>
    <ul>
        <li><b>Data Warehousing:</b> Implemented Snowflake solutions for structured (CSV) and semi-structured (JSON, XML) formats[cite: 24].</li>
        <li><b>Automation:</b> Developed high-efficiency pipelines using Snowpipe and External Integration for auto-ingestion[cite: 25].</li>
        <li><b>Transformation:</b> Authored advanced SQL for schema creation and metadata management[cite: 26].</li>
        <li><b>Supply Chain:</b> Delivered Power BI reporting for tracking key US FMCG client metrics[cite: 28].</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# TCS
st.markdown(f"""
<div class="glass-card">
    <div class="job-title">Data Engineer</div>
    <div class="company-name">Tata Consultancy Services, Pune</div>
    <div class="date-tag">NOV 2020 — OCT 2023</div>
    <br>
    <ul>
        <li><b>ERP Migration:</b> Deployed ADF CDC pipelines for SAP migration, reducing ETL cycle time by 30%.</li>
        <li><b>FinOps:</b> Created Analytics Dashboards using Azure Monitor APIs to support cost governance.</li>
        <li><b>Optimization:</b> Enhanced Synapse workflows with PySpark/SQL for finance and compliance operations[cite: 32].</li>
        <li><b>Retail Analytics:</b> Designed competitor insight dashboards for European retail clients using SQL and Power BI[cite: 36].</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- EDUCATION & CERTIFICATIONS ---
st.divider()
c1, c2 = st.columns(2)

with c1:
    st.write("## 🎓 Education")
    st.markdown(f"""
    **B.Tech in Mechanical Engineering** [cite: 38]  
    Medi-caps University (2016-2020) | **CGPA: 7.95** [cite: 38, 45]
    
    - **Higher Secondary:** 78.9% [cite: 39]
    - **Secondary:** CGPA: 9.4 [cite: 40]
    """)

with c2:
    st.write("## 🏆 Certifications")
    st.markdown("""
    * ✅ **Snow Pro Core Certified** [cite: 42]
    * ✅ **Databricks Certified Data Engineer Associate** [cite: 43]
    * ✅ **MS Fabric Data Engineer Associate (DP-700)** [cite: 44]
    * ✅ **MS Power BI Data Analyst (PL-300)** [cite: 48]
    * ✅ **MS Data Engineering on Azure (DP-203)** [cite: 49]
    * ✅ **MS Fabric Analytics Engineer Associate (DP-600)** [cite: 50]
    """)

st.markdown("<br><center style='opacity:0.4;'>Built with Streamlit • 2026 Portfolio</center>", unsafe_allow_html=True)
