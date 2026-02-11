import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Priyam Sachan | Data Engineer Portfolio",
    page_icon="📊",
    layout="wide"
)

# 2. Robust CSS for Background and Glassmorphism
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #334155 100%);
        color: #e2e8f0;
    }
    
    /* Card Styling */
    div.stExpander {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        margin-bottom: 10px;
    }

    /* Custom Header Colors */
    h1, h2, h3 {
        color: #60a5fa !important;
    }

    /* Text color fix for clarity */
    .stMarkdown p {
        color: #cbd5e1;
    }

    /* Sidebar color */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=100)
    st.title("Contact Me")
    st.write("📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")
    st.write("📞 +91 8840750905")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan)")
    st.divider()
    st.info("Available for Data Engineering opportunities.")

# --- MAIN CONTENT ---
col1, col2 = st.columns([3, 1])

with col1:
    st.title("PRIYAM SACHAN")
    st.subheader("Senior Data Engineer")
    st.write("Expertise in Cloud Migration, Big Data ETL, and Medallion Architectures.")

# --- SKILLS SECTION ---
st.header("🛠️ Technical Expertise")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("### Languages")
    st.write("Python, SQL, PySpark, Scala")
    st.markdown("### Databases")
    st.write("MySQL, SQL Server, CosmosDB, S3, ADLS")

with s2:
    st.markdown("### Cloud & Big Data")
    st.write("Azure (ADF, Databricks, Synapse, Fabric), Snowflake, Snowpark, AWS")

with s3:
    st.markdown("### BI & Tools")
    st.write("Power BI, Git, JIRA, Generative AI, Prompt Engineering")

st.divider()

# --- WORK EXPERIENCE ---
st.header("💼 Professional Experience")

# Mastercard
with st.expander("🔹 Data Engineer | Mastercard", expanded=True):
    st.markdown("#### Jan 2025 - Present")
    st.markdown("""
    - **Cloud Migration**: Architected on-prem Oracle to AWS migration.
    - **ETL/ELT**: Deployed incremental pipelines using **Apache Nifi**.
    - **Optimization**: Optimized S3 data into **Parquet** using Databricks notebooks.
    - **Architecture**: Implemented **Medallion Architecture** (Bronze/Silver/Gold).
    """)

# EY
with st.expander("🔹 Data Engineer | Ernst & Young"):
    st.markdown("#### Nov 2023 - Jan 2025")
    st.markdown("""
    - **Warehousing**: Delivered Snowflake solutions for structured and semi-structured data.
    - **Automation**: Implemented **Snowpipe** for automated ingestion.
    - **Analytics**: Built Supply Chain dashboards for US FMCG clients using Power BI.
    """)

# TCS
with st.expander("🔹 Data Engineer | Tata Consultancy Services"):
    st.markdown("#### Nov 2020 - Oct 2023")
    st.markdown("""
    - **Efficiency**: Reduced ETL cycle time by **30%** via ADF CDC for SAP migration.
    - **Governance**: Built FinOps Analytics Dashboards for cost management.
    - **Retail Analytics**: Designed competitor insight tools for European retail markets.
    """)

st.divider()

# --- EDUCATION & CERTIFICATIONS ---
e1, e2 = st.columns(2)

with e1:
    st.header("🎓 Education")
    st.markdown("**B.Tech in Mechanical Engineering**")
    st.write("Medi-caps University (2016 - 2020)")
    st.write("CGPA: 7.95")

with e2:
    st.header("📜 Certifications")
    st.write("🏆 Snow Pro Core")
    st.write("🏆 Databricks Data Engineer Associate")
    st.write("🏆 MS Azure Data Engineer (DP-203)")
    st.write("🏆 MS Fabric Engineer (DP-600/DP-700)")

st.divider()
st.markdown("<center>Built with Streamlit | 2026</center>", unsafe_allow_html=True)
