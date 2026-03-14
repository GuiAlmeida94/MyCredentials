import streamlit as st
import os

# --- Page Setup ---
st.set_page_config(
    page_title="Guilherme Oyakawa - Credentials", 
    page_icon="📜", 
    layout="wide"
)

# --- Technical function to find files safely (Case Insensitive) ---
def find_file(filename):
    if not filename: return None
    try:
        files_in_dir = os.listdir('.')
        for f in files_in_dir:
            if f.lower() == filename.lower():
                return f
    except: return None
    return None

# --- Custom CSS ---
st.markdown("""
    <style>
    .cert-card {
        border: 1px solid #e6e9ef;
        border-radius: 10px;
        padding: 20px;
        background-color: #f8f9fa;
        margin-bottom: 20px;
        min-height: 250px;
    }
    .stDownloadButton > button {
        width: 100%;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: CV Downloads & Filters ---
with st.sidebar:
    st.header("📄 Download CV / Resume")
    
    # English Version
    cv_en = "English-Guilherme-Oyakawa-Almeida-2026.pdf"
    actual_en = find_file(cv_en)
    if actual_en:
        with open(actual_en, "rb") as f:
            st.download_button(
                label="🇬🇧 Download CV (English)",
                data=f,
                file_name=actual_en,
                mime="application/pdf"
            )
    
    # Portuguese Version
    cv_pt = "Portugues-Guilherme-Oyakawa-Almeida-2026.pdf"
    actual_pt = find_file(cv_pt)
    if actual_pt:
        with open(actual_pt, "rb") as f:
            st.download_button(
                label="🇧🇷 Download CV (Português)",
                data=f,
                file_name=actual_pt,
                mime="application/pdf"
            )
    
    if not actual_en and not actual_pt:
        st.warning("⚠️ CV files not found in GitHub.")

    st.divider()
    st.header("🔍 Filters")
    
    certificates = [
        {
            "title": "Professional Certificate in Data Analytics", 
            "file": None, 
            "issuer": "Imperial College Business School", 
            "category": "Data BI",
            "status": "In Progress",
            "progress": 90
        },
        {
            "title": "Master in Data Science", 
            "file": "Certificate - GUILHERME OYAKAWA DE ALMEIDA.jpg", 
            "issuer": "Rome Business School", 
            "category": "Academic",
            "status": "Completed"
        },
        {
            "title": "Power BI Data Analyst", 
            "file": "DataCampCertification_PBI.jpg", 
            "issuer": "DataCamp", 
            "category": "Data BI",
            "status": "Completed"
        },
        {
            "title": "SQL Data Analyst", 
            "file": "DataCampCertification_SQL.jpg", 
            "issuer": "DataCamp", 
            "category": "SQL",
            "status": "Completed"
        },
        {
            "title": "Python Data Analyst", 
            "file": "certificate_python Data Analyst.jpg", 
            "issuer": "DataCamp", 
            "category": "Python",
            "status": "Completed"
        },
        {
            "title": "Academic Transcript", 
            "file": "Transcript - Guilherme Oyakawa De Almeida.jpg", 
            "issuer": "Rome Business School", 
            "category": "Academic",
            "status": "Completed"
        },
    ]
    
    categories = ["All"] + sorted(list(set(c["category"] for c in certificates)))
    selected_category = st.selectbox("Select Category:", categories)

# --- Main Gallery ---
st.title("📜 Professional Credentials")
