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
    st.header("📄 Downloads")
    
    # English Version CV
    cv_en = "English-Guilherme-Oyakawa-Almeida-2026.pdf"
    actual_en = find_file(cv_en)
    if actual_en:
        with open(actual_en, "rb") as f:
            st.download_button(label="🇬🇧 Download CV (English)", data=f.read(), file_name=actual_en, mime="application/pdf")
    
    # Portuguese Version CV
    cv_pt = "Portugues-Guilherme-Oyakawa-Almeida-2026.pdf"
    actual_pt = find_file(cv_pt)
    if actual_pt:
        with open(actual_pt, "rb") as f:
            st.download_button(label="🇧🇷 Download CV (Português)", data=f.read(), file_name=actual_pt, mime="application/pdf")

    # Italian Version CV
    cv_it = "Italiano-Guilherme-Oyakawa-Almeida-2026.pdf"
    actual_it = find_file(cv_it)
    if actual_it:
        with open(actual_it, "rb") as f:
            st.download_button(label="🇮🇹 Download CV (Italiano)", data=f.read(), file_name=actual_it, mime="application/pdf")
    
    st.divider()
    
    # NOVO: Certificado de Inglês em Destaque
    st.header("🌐 Language Proficiency")
    eng_cert = "English_Certificate.pdf"
    actual_eng = find_file(eng_cert)
    if actual_eng:
        with open(actual_eng, "rb") as f:
            st.download_button(label="🏆 English Certificate (C1 Advanced)", data=f.read(), file_name=actual_eng, mime="application/pdf")
        st.caption("EF SET Score: 69/100 (C2 in Reading, Listening & Speaking)")

    st.divider()
    st.header("🔍 Filters")
    
    certificates = [
        {
            "title": "English Certificate - C1 Advanced", 
            "file": "English_Certificate.pdf", 
            "issuer": "EF SET", 
            "category": "Languages",
            "status": "Completed"
        },
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
            "title": "Master in Data Science - Academic Transcript", 
            "file": "Transcript - Guilherme Oyakawa De Almeida.pdf",
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
        }
    ]
    
    categories = ["All"] + sorted(list(set(c["category"] for c in certificates)))
    selected_category = st.selectbox("Select Category:", categories)

# --- Main Gallery ---
st.title("📜 Professional Credentials")
st.write("Verified certificates and academic background.")

filtered_certs = [c for c in certificates if selected_category == "All" or c["category"] == selected_category]
cols = st.columns(2)

for i, cert in enumerate(filtered_certs):
    with cols[i % 2]:
        st.markdown(f"""<div class="cert-card">
            <h3>{cert['title']}</h3>
            <p><b>Issuer:</b> {cert['issuer']} | <b>Category:</b> {cert['category']}</p>
        </div>""", unsafe_allow_html=True)
        
        if cert.get("status") == "In Progress":
            st.info(f"⏳ **Status:** {cert['status']}")
            st.progress(cert['progress'] / 100)
            st.caption(f"Progress: {cert['progress']}%")
        else:
            actual_file = find_file(cert['file'])
            if actual_file:
                # Se for PDF, mostramos um ícone ou mensagem, se for imagem, mostramos a imagem
                if actual_file.lower().endswith('.pdf'):
                    st.info("📄 PDF Document Available for Download")
                else:
                    st.image(actual_img if 'actual_img' in locals() else actual_file, use_container_width=True)
                
                with open(actual_file, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Download Document",
                        data=f.read(),
                        file_name=actual_file,
                        key=f"btn_{i}"
                    )
            else:
                st.error(f"⚠️ Not found: {cert['file']}")
        st.divider()
