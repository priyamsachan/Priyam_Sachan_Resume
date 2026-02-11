import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Priyam Sachan | Data Engineer Portfolio",
    page_icon="📊",
    layout="wide"
)

# 2. Enhanced CSS for Background and Same-Color Expanders
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #334155 100%);
        color: #e2e8f0;
    }
    
    /* TARGETING THE EXPANDER */
    /* This ensures the expander doesn't turn white when opened */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
    }

    /* Target the header of the expander */
    div[data-testid="stExpander"] summary {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #60a5fa !important;
    }

    /* Target the content area of the expander when open */
    div[data-testid="stExpander"] [data-testid="stVerticalBlock"] {
        background-color: transparent !important;
    }

    /* Change hover effect for expander */
    div[data-testid="stExpander"] summary:hover {
        background-color: rgba(255, 255, 255, 0.1) !important;
    }

    /* Custom Header Colors */
    h1, h2, h3 {
        color: #60a5fa !important;
    }

    /* Text color for standard markdown */
    .stMarkdown p, li {
        color: #cbd5e1 !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.9);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Contact Me")
    st.write("📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")
    st.write("📞 +91 8840750905")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan)")
    st.divider()
    st.info("Expert in Azure, Snowflake, and Databricks.")

# --- MAIN CONTENT ---
st.title("PRIYAM SACHAN")
st.subheader("Senior Data Engineer")
st.write("Specializing in Medallion Architecture and Cloud Migrations.")

st.divider()

# --- SKILLS ---
st.header("🛠️ Technical Expertise")
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("### Languages")
    st.write("Python, SQL, PySpark, Scala")
with s2:
    st.markdown("### Cloud & Big Data")
    st.write("Azure, Snowflake, Databricks, AWS, Fabric")
with s3:
    st.markdown("### Databases & Tools")
    st.write("CosmosDB, SQL Server, Power BI, Git")

st.divider()

# --- WORK EXPERIENCE ---
st.header("💼 Professional Experience")

# Mastercard
with st.expander("🔹 Data Engineer | Mastercard (2025 - Present)", expanded=True):
    st.markdown("""
    - **
