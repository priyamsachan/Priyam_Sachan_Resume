import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Priyam Sachan | Senior Data Engineer",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced Professional Styling (CSS)
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

    .res-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .res-card:hover {
        border-color: #38bdf8;
        background: rgba(56, 189, 248, 0.05);
        transform: translateY(-2px);
    }

    .skill-badge {
        display: inline-block;
        padding: 5px 14px;
        border-radius: 8px;
        background: #0ea5e9;
        color: white;
        margin: 4px;
        font-size: 12px;
        font-weight: 600;
    }

    h1, h2 {
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=120)
    st.title("Priyam Sachan")
    st.markdown("📍 **Greater Noida, India**")
    st.write("📧 [Email Me](mailto:priyamsachan12051997@gmail.com)")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/priyam-sachan)")
    st.divider()
    st.download_button("📄 Download CV", "Binary Content", file_name="Priyam_Sachan_DE.pdf")

# --- HERO ---
st.title("Senior Data Engineer")
st.markdown("Specializing in **Medallion Architectures**, **Cloud Migrations**, and **Scalable ETL/ELT** pipelines.")

# --- TECHNICAL ECOSYSTEM ---
st.write("## 🛠️ Technical Ecosystem")
col_a, col_b, col_c = st.columns(3)

def create_skill_html(skills):
    badges = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
    return f"<div>{badges}</div>"

with col_a:
    st.markdown("### 💻 Engineering")
    # FIXED LINE BELOW
    st.markdown(create_skill_html(["Python", "SQL", "PySpark", "Scala", "Java"]), unsafe_allow_html=True)

with col_b:
    st.markdown("### ☁️ Cloud & Warehouse")
    st.markdown(create_skill_html(["Azure", "AWS", "Snowflake", "Databricks", "Fabric"]), unsafe_allow_html=True)

with col_c:
    st.markdown("### 🤖 Orchestration")
    st.markdown(create_skill_html(["Nifi", "Airflow", "ADF", "Git", "Power BI"]), unsafe_allow_html=True)

st.divider()

# --- EXPERIENCE ---
st.write("## 💼 Professional Experience")

# Mastercard
st.markdown("""
<div class="res-card">
    <h3 style="margin:0; color:#38bdf8;">Mastercard | Senior Data Engineer</h3>
    <p style="color:#94a3b8;">Jan 2025 - Present</p>
    <ul>
        <li><b>Cloud Migration:</b> Leading Oracle to AWS Glue/Nifi migration.</li>
        <li><b>Architecture:</b> Building 1TB+ daily Medallion Lakehouse layers.</li>
    </ul>
</div>
""", unsafe_allow_html=True)



# EY
st.markdown("""
<div class="res-card">
    <h3 style="margin:0; color:#38bdf8;">EY | Data Engineer</h3>
    <p style="color:#94a3b8;">Nov 2023 - Jan 2025</p>
    <ul>
        <li><b>Optimization:</b> Reduced Snowflake query latency by 45%.</li>
        <li><b>Solutions:</b> End-to-end Supply Chain pipelines for US FMCG.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# TCS
st.markdown("""
<div class="res-card">
    <h3 style="margin:0; color:#38bdf8;">TCS | Data Engineer</h3>
    <p style="color:#94a3b8;">Nov 2020 - Oct 2023</p>
    <ul>
        <li><b>SAP Migration:</b> Built CDC pipelines using ADF.</li>
        <li><b>FinOps:</b> Saved $12k/month in cloud optimization.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- EDUCATION & CERTS ---
st.divider()
l, r = st.columns(2)
with l:
    st.write("## 🎓 Education")
    st.write("**B.Tech** | Medi-caps University | CGPA: 7.95")
with r:
    st.write("## 🏆 Certifications")
    st.write("SnowPro Core • DP-203 • Databricks Associate • DP-600")

st.markdown("<br><center style='opacity:0.5;'>Built with Streamlit 2026</center>", unsafe_allow_html=True)
