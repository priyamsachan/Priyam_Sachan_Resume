import streamlit as st

# 1. Page Config (Must be the first Streamlit command)
st.set_page_config(
    page_title="Priyam Sachan | Portfolio",
    page_icon="📊",
    layout="wide"
)

# 2. Advanced CSS for Background and Styling
st.markdown("""
    <style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #60a5fa 100%);
        color: white;
    }
    
    /* Card-like containers for content */
    div.stExpander, div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Customizing Headings */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    /* Divider color */
    hr {
        border-top: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Links */
    a {
        color: #93c5fd !important;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("PRIYAM SACHAN")
    st.subheader("Senior Data Engineer")
    st.write("📍 Pune, India")
    st.markdown("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan) | 📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")

with col2:
    st.write("### Contact")
    st.write("📞 +91 8840750905")

st.divider()

# --- TECHNICAL SKILLS ---
st.header("🛠️ Technical Stack")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("#### Languages & Core")
    st.write("- Python, SQL, PySpark\n- Spark, Scala\n- Pandas, NumPy")

with c2:
    st.markdown("#### Cloud & Data")
    st.write("- Azure (ADF, Databricks, Synapse)\n- Snowflake, MS Fabric\n- AWS S3, Apache Nifi")

with c3:
    st.markdown("#### BI & Utilities")
    st.write("- Power BI, Data Modeling\n- Git, JIRA, Postman\n- Generative AI & Copilot")

st.divider()

# --- WORK EXPERIENCE ---
st.header("💼 Work Experience")

# Mastercard
with st.expander("🔹 Data Engineer - Mastercard (Jan 2025 - Present)", expanded=True):
    st.markdown("""
    * **Architecture**: Architected migration from on-prem Oracle to **AWS Cloud**.
    * **Orchestration**: Deployed incremental ETL pipelines using **Apache Nifi**.
    * **Optimization**: Processed raw S3 data into **Parquet** via Databricks (Python/Scala).
    * **Framework**: Established **Medallion Data Architecture** (Bronze/Silver/Gold).
    """)

# EY
with st.expander("🔹 Data Engineer - Ernst & Young (Nov 2023 - Jan 2025)"):
    st.markdown("""
    * **Snowflake**: Implemented solutions for structured and semi-structured data (JSON, XML).
    * **Automation**: Used **Snowpipe** for automated, incremental data loading.
    * **BI**: Delivered Supply Chain insights for a US FMCG client using **Power BI**.
    """)

# TCS
with st.expander("🔹 Data Engineer - Tata Consultancy Services (Nov 2020 - Oct 2023)"):
    st.markdown("""
    * **Efficiency**: Reduced ETL cycle time by **30%** using ADF CDC for SAP migration.
    * **FinOps**: Built Analytics Dashboard using Azure Monitor APIs for cost governance.
    * **Analytics**: Designed
