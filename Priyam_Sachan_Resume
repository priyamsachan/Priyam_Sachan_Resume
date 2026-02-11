import streamlit as st

# Page Configuration
st.set_page_config(page_title="Priyam Sachan | Data Engineer", page_icon="📊", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stBadge {
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_index=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Priyam Sachan")
    st.subheader("Senior Data Engineer")
    st.write("📍 Pune, India")
    st.write("📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan)")

with col2:
    st.write(f"📞 +91 8840750905")

st.divider()

# --- SUMMARY / TECHNICAL LEADERSHIP ---
st.header("Technical Leadership & Core Competencies")
st.write("Lead technical initiatives, mentor team members in best practices, strategic thinking, and cross-functional collaboration.")

# --- TECHNICAL SKILLS ---
st.header("Technical Skills")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    st.bold("Languages & Libraries")
    st.write("Python, SQL, PySpark, Spark, Scala, Pandas, NumPy, Matplotlib")

with col_s2:
    st.bold("Big Data & Cloud")
    st.write("Azure (ADF, Databricks, Synapse, Fabric), Snowflake, AWS (S3), Hadoop, Snowpark")

with col_s3:
    st.bold("Databases & Tools")
    st.write("MySQL, SQL Server, CosmosDB, Power BI, Git, JIRA, Generative AI (Prompt Engineering)")

st.divider()

# --- WORK EXPERIENCE ---
st.header("Professional Experience")

# Mastercard
with st.expander("Data Engineer | Mastercard", expanded=True):
    st.subheader("Jan 2025 - Present")
    st.markdown("""
    - **Cloud Migration**: Architected end-to-end data migration from on-prem Oracle to AWS Cloud.
    - **Orchestration**: Designed incremental ETL pipelines using **Apache Nifi** to ingest transaction events into S3.
    - **Processing**: Developed Databricks notebooks (Python/Scala) to optimize raw S3 data into **Parquet** format.
    - **Architecture**: Established a **Medallion Architecture** (Bronze/Silver/Gold) to ensure data quality.
    - **Modeling**: Constructed Canonical Data Models (CDM) in the Gold layer with Fact and Dimension tables.
    """)

# EY
with st.expander("Data Engineer | Ernst & Young"):
    st.subheader("Nov 2023 - Jan 2025")
    st.markdown("""
    - **Data Warehousing**: Implemented **Snowflake** solutions for structured (CSV) and semi-structured (JSON, XML) data.
    - **Automation**: Utilized **Snowpipe** and Storage Integration for automated, incremental data loading.
    - **Reporting**: Delivered Supply Chain insights using Power BI for a US FMCG client.
    - **Advanced SQL**: Authored scripts for schema creation, metadata management, and auditing.
    """)

# TCS
with st.expander("Data Engineer | Tata Consultancy Services"):
    st.subheader("Nov 2020 - Oct 2023")
    st.markdown("""
    - **ERP Migration**: Deployed Azure Data Factory CDC connectors for SAP migration, reducing ETL cycle time by **30%**.
    - **Optimization**: Enhanced efficiency on **Azure Synapse** using PySpark and Advanced SQL.
    - **FinOps**: Created a FinOps Analytics Dashboard using Azure Monitor APIs for cost governance.
    - **Retail Analytics**: Designed competitor insight dashboards empowering pricing optimization for European clients.
    """)

st.divider()

# --- CERTIFICATIONS ---
st.header("Certifications")
c1, c2 = st.columns(2)
with c1:
    st.write("🏆 **Snow Pro Core Certified**")
    st.write("🏆 **Databricks Certified Data Engineer Associate**")
    st.write("🏆 **MS Fabric Data Engineer Associate (DP-700)**")
with c2:
    st.write("🏆 **MS Power BI Data Analyst (PL-300)**")
    st.write("🏆 **MS Data Engineering on Azure (DP-203)**")
    st.write("🏆 **MS Fabric Analytics Engineer Associate (DP-600)**")

st.divider()

# --- EDUCATION ---
st.header("Education")
st.write("**Bachelor of Technology in Mechanical Engineering** | Medi-caps University")
st.write("CGPA: 7.95 (2016 - 2020)")

# --- FOOTER ---
st.caption("Built with Streamlit • 2026")
