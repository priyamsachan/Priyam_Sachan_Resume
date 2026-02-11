import streamlit as st

# 1. Page Config (Must be first)
st.set_page_config(
    page_title="Priyam Sachan | Data Engineer Portfolio",
    page_icon="📊",
    layout="wide"
)

# 2. CSS for Background and Expander Styling
st.markdown("""
    <style>
    /* Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Expander - No White Background */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }

    /* Expander Header */
    div[data-testid="stExpander"] summary {
        color: #60a5fa !important;
        font-weight: bold;
    }

    /* Text inside expander */
    div[data-testid="stExpander"] .stMarkdown p {
        color: #cbd5e1 !important;
    }

    /* Sidebar color */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
    }

    /* Title colors */
    h1, h2, h3 {
        color: #60a5fa !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Contact Details")
    st.write("📍 Pune, India")
    st.write("📞 +91 8840750905")
    st.write("📧 [Email Me](mailto:priyamsachan12051997@gmail.com)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan)")
    st.divider()
    st.write("### Top Certs")
    st.caption("Snow Pro Core")
    st.caption("Databricks Associate")
    st.caption("Azure DP-203")

# --- HEADER ---
st.title("PRIYAM SACHAN")
st.subheader("Senior Data Engineer")
st.write("Specializing in Medallion Architecture, Cloud Migration (AWS/Azure), and Snowflake.")

st.divider()

# --- SKILLS ---
st.header("🛠️ Technical Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Languages")
    st.write("Python, SQL, PySpark, Spark, Scala")
    st.markdown("### Databases")
    st.write("MySQL, SQL Server, CosmosDB, S3, ADLS")

with col2:
    st.markdown("### ETL & Cloud")
    st.write("Azure (ADF, Databricks, Synapse, Fabric)")
    st.write("Snowflake, Snowpark, AWS, Apache Nifi")

with col3:
    st.markdown("### BI & Tools")
    st.write("Power BI, Data Modeling, DAX")
    st.write("JIRA, Git, Generative AI, Prompt Engineering")

st.divider()

# --- PROFESSIONAL EXPERIENCE ---
st
