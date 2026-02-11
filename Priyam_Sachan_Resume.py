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

# --- SIDEBAR: CONTACT & PERSONAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=110)
    st.title("Priyam Sachan")
    st.markdown("📍 **Pune, India**")
    st.write(f"📞 { '+91 8840750905' }")
    st.write(f"📧 [Email Me](mailto:{'priyamsachan12051997@gmail.com'})")
    st.write(f"🔗 [LinkedIn Profile](https://{'linkedin.com/in/priyam-sachan'})")
    
    st.divider()
    st.markdown("### Technical Leadership")
    st.caption("Lead technical initiatives, Mentoring, Strategic thinking, Collaboration")
    
    st.divider()
    st.download_button("📄 Download Full Resume", "Resume PDF Content", file_name="Priyam_Sachan_Resume.pdf")

# --- HERO SECTION ---
st.title("Senior Data Engineer")
st.markdown("""
    Expert Data Engineer with a proven track record in **Architecting Cloud Migrations**, **Medallion Data Lakehouses**, and **Scalable ETL Pipelines**. 
    Specializing in transforming complex on-premise environments into optimized, cloud-native analytical ecosystems.
""")

# --- TECHNICAL SKILLS (Complete List) ---
st.write("## 🛠️ Technical Skills")
col_a, col_b, col_c = st.columns(3)

def skill_badges(skills):
    return "".join([f'<span class="skill-badge">{s}</span>' for s in skills])

with col_a:
    st.markdown("### 💻 Languages & Frameworks")
    st.markdown(skill_badges(["Python", "SQL", "PySpark", "Spark", "Scala", "Pandas", "NumPy", "Matplotlib"]), unsafe_allow_html=True)

with col_b:
    st.markdown("### ☁️ Data Engineering & Cloud")
    st.markdown(skill_badges(["Azure Data Factory", "Synapse", "Databricks", "Snowflake", "Microsoft Fabric", "Snowpark", "AWS S3", "Apache Nifi"]), unsafe_allow_html=True)

with col_c:
    st.markdown("### 📊 BI & Utilities")
    st.markdown(skill_badges(["Power BI", "DAX", "Data Modeling", "Git", "JIRA", "Postman", "Generative AI", "Copilot"]), unsafe_allow_html=True)

st.divider()

# --- WORK EXPERIENCE (Full Detail) ---
st.write("## 💼 Professional Experience")

# 1. Mastercard
with st.container():
    st.markdown(f"""
    <div class="res-card">
        <div class="job-header">
            <h3>Data Engineer | Mastercard</h3>
            <span class="exp-date">Jan 2025 - Present</span>
        </div>
        <ul>
            <li><b>Cloud Architecture:</b> Architected end-to-end data migration from on-prem <b>Oracle</b> to <b>AWS Cloud</b>. [cite: 15]</li>
            <li><b>Pipeline Engineering:</b> Deployed incremental ETL leveraging <b>Apache Nifi</b> to ingest transaction events to <b>Amazon S3 (Bronze)</b>. [cite: 16]</li>
            <li><b>Medallion Implementation:</b> Established Bronze/Silver/Gold architecture ensuring high data quality and standardization. [cite: 18]</li>
            <li><b>Processing Power:</b> Developed <b>Databricks</b> notebooks (Python/Scala) to convert raw S3 data into optimized <b>Parquet</b>. [cite: 17]</li>
            <li><b>Data Modeling:</b> Constructed <b>Canonical Data Models (CDM)</b> in the Gold layer with Fact and Dimension tables for BI. [cite: 20]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# 2. EY
with st.container():
    st.markdown(f"""
    <div class="res-card">
        <div class="job-header">
            <h3>Data Engineer | Ernst & Young (EY)</h3>
            <span class="exp-date">Nov 2023 - Jan 2025</span>
        </div>
        <ul>
            <li><b>Snowflake Warehousing:</b> Designed solutions integrating structured (CSV) and semi-structured (JSON, XML) data for US FMCG clients. [cite: 24]</li>
            <li><b>Automation:</b> Utilized <b>Snowpipe</b> and Storage Integration for automated, incremental data loading. </li>
            <li><b>Business Impact:</b> Delivered <b>Supply Chain Reporting</b> in Power BI to track key weekly/monthly metrics. [cite: 28]</li>
            <li><b>Transformation:</b> Authored advanced SQL scripts for schema creation and comprehensive metadata auditing. [cite: 26]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 3. TCS
with st.container():
    st.markdown(f"""
    <div class="res-card">
        <div class="job-header">
            <h3>Data Engineer | Tata Consultancy Services (TCS)</h3>
            <span class="exp-date">Nov 2020 - Oct 2023</span>
        </div>
        <ul>
            <li><b>SAP Migration:</b> Built scalable pipelines using <b>Azure Data Factory CDC</b>, reducing ETL cycle time by <b>30%</b>. </li>
            <li><b>FinOps Leadership:</b> Created <b>FinOps Analytics Dashboards</b> using Azure Monitor APIs for cost governance. [cite: 34]</li>
            <li><b>Workload Optimization:</b> Enhanced efficiency on <b>Azure Synapse</b> using PySpark and Advanced SQL for compliance operations. [cite: 32]</li>
            <li><b>Strategic Insights:</b> Designed competitor insight dashboards for European retail clients using SQL and Power BI. [cite: 36]</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- EDUCATION & CERTIFICATIONS ---
st.write("---")
ed_col, cert_col = st.columns([1, 1])

with ed_col:
    st.write("## 🎓 Education")
    st.markdown(f"""
    **Bachelor of Technology | Mechanical Engineering** *Medi-caps University* (2016 - 2020)  
    **CGPA: 7.95** [cite: 38, 45]
    
    **Higher Secondary:** 78.9% [cite: 39]  
    **Secondary:** CGPA: 9.4 [cite: 40]
    """)

with cert_col:
    st.write("## 🏆 Certifications")
    cert_list = [
        "Snow Pro Core Certified [cite: 42]",
        "Databricks Certified Data Engineer Associate [cite: 43]",
        "MS Fabric Data Engineer Associate (DP-700) [cite: 44]",
        "MS Power BI Data Analyst (PL-300) [cite: 48]",
        "MS Data Engineering on Azure (DP-203) [cite: 49]",
        "MS Fabric Analytics Engineer Associate (DP-600) [cite: 50]"
    ]
    for cert in cert_list:
        st.markdown(f"✅ {cert}")

# --- FOOTER ---
st.write("---")
st.markdown("<center style='opacity:0.6; font-size: 13px;'>Built by Priyam Sachan | Streamlit & Data Engineering Portfolio | 2026</center>", unsafe_allow_html=True)
