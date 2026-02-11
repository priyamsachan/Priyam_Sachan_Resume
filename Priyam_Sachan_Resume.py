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
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at top left, #0f172a, #1e293b);
        color: #f1f5f9;
    }

    /* Professional Card Styling */
    .res-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .res-card:hover {
        border-color: #38bdf8;
        background: rgba(56, 189, 248, 0.05);
    }

    /* Skill Badge Styling */
    .skill-badge {
        display: inline-block;
        padding: 5px 14px;
        border-radius: 8px;
        background: #0ea5e9;
        color: white;
        margin: 4px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    /* Section Headers */
    h1, h2 {
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    /* Custom Divider */
    hr {
        margin: 2em 0;
        border: 0;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Contact & Links) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=120)
    st.title("Priyam Sachan")
    st.markdown("📍 **Greater Noida, India**")
    
    st.markdown("### Let's Connect")
    st.write("📧 [priyamsachan12051997@gmail.com](mailto:priyamsachan12051997@gmail.com)")
    st.write("🔗 [LinkedIn Profile](https://linkedin.com/in/priyam-sachan)")
    st.write("🐙 [GitHub Portfolio](https://github.com)")
    
    st.divider()
    st.download_button(
        label="📄 Download Official CV",
        data="Binary Content Here",
        file_name="Priyam_Sachan_DataEngineer.pdf",
        mime="application/pdf"
    )

# --- MAIN HERO SECTION ---
c1, c2 = st.columns([3, 1])
with c1:
    st.title("Senior Data Engineer")
    st.markdown("""
        **Bridging the gap between raw data and business intelligence.** Specializing in building high-performance data lakes, automated ETL/ELT pipelines, 
        and cloud-native architectures for global enterprises like Mastercard and EY.
    """)

# --- TECHNICAL ECOSYSTEM ---
st.write("## 🛠️ Technical Ecosystem")
col_a, col_b, col_c = st.columns(3)

def create_skill_html(skills):
    badges = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
    return f"<div>{badges}</div>"

with col_a:
    st.markdown("### 💻 Engineering")
    st.markdown(create_skill_html(["Python", "SQL", "PySpark", "Scala
