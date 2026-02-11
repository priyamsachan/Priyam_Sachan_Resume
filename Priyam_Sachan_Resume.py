import streamlit as st
import textwrap

# 1. MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Priyam Sachan | Data Engineer", page_icon="📊", layout="wide")

# 2. FIX: Ensure CSS is not indented inside the markdown string
css_code = textwrap.dedent("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stBadge {
        font-size: 14px;
    }
    </style>
    """)
st.markdown(css_code, unsafe_allow_html=True)

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

# --- SKILLS & EXPERIENCE ---
st.header("Technical Skills")
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.markdown("**Languages & Libraries**")
    st.write("Python, SQL, PySpark, Spark, Scala, Pandas, NumPy, Matplotlib")
with col_s2:
    st.markdown("**Big Data & Cloud**")
    st.write("Azure, Snowflake, AWS (S3), Hadoop, Snowpark")
with col_s3:
    st.markdown("**Databases & Tools**")
    st.write("MySQL, SQL Server, CosmosDB, Power BI, Git, JIRA")

st.divider()

st.header("Professional Experience")
with st.expander("Data Engineer | Mastercard", expanded=True):
    st.caption("Jan 2025 - Present")
    st.markdown("""
    - Architected end-to-end data migration from on-prem Oracle to AWS.
    - Designed incremental ETL pipelines using **Apache Nifi**.
    - Developed Databricks notebooks to optimize data into **Parquet**.
    """)

with st.expander("Data Engineer | Ernst & Young"):
    st.caption("Nov 2023 - Jan 2025")
    st.markdown("""
    - Implemented Snowflake solutions for structured and semi-structured data.
    - Utilized Snowpipe for automated, incremental data loading.
    """)

# ... (rest of your resume details)
