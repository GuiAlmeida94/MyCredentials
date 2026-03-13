import streamlit as st
import os

# --- Page Setup ---
st.set_page_config(
    page_title="Guilherme Oyakawa - Credentials", 
    page_icon="📜", 
    layout="wide"
)

# --- Technical function to find files safely ---
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
    }
    .stDownloadButton > button {
        width: 100%;
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
        st.warning("⚠️ CV files not found. Check names in GitHub.")

    st.divider()
    st.header("🔍 Filters")
    
    certificates = [
        {"title": "Master in Data Science", "file": "Certificate - GUILHERME OYAKAWA DE ALMEIDA.jpg", "issuer": "Rome Business School", "category": "Academic"},
        {"title": "Power BI Data Analyst", "file": "DataCampCertification_PBI.jpg", "issuer": "DataCamp", "category": "Data BI"},
        {"title": "SQL Data Analyst", "file": "DataCampCertification_SQL.jpg", "issuer": "DataCamp", "category": "SQL"},
        {"title": "Python Data Analyst", "file": "certificate_python Data Analyst.jpg", "issuer": "DataCamp", "category": "Python"},
        {"title": "Academic Transcript", "file": "Transcript - Guilherme Oyakawa De Almeida.jpg", "issuer": "Rome Business School", "category": "Academic"},
    ]
    
    categories = ["All"] + sorted(list(set(c["category"] for c in certificates)))
    selected_category = st.selectbox("Category:", categories)

# --- Main Gallery ---
st.title("📜 Professional Credentials")
st.write("Verified certificates and academic background.")

filtered_certs = [c for c in certificates if selected_category == "All" or c["category"] == selected_category]
cols = st.columns(2)

for i, cert in enumerate(filtered_certs):
    with cols[i % 2]:
        actual_img = find_file(cert['file'])
        if actual_img:
            st.markdown(f'<div class="cert-card"><h3>{cert["title"]}</h3><p><b>{cert["issuer"]}</b></p></div>', unsafe_allow_html=True)
            st.image(actual_img, use_container_width=True)
            with open(actual_img, "rb") as f:
                st.download_button(label=f"⬇️ Download Certificate", data=f, file_name=actual_img, key=f"btn_{i}")
        st.divider()
