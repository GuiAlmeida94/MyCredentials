import streamlit as st

st.set_page_config(page_title="Guilherme Oyakawa - Credentials", page_icon="📜", layout="wide")

# Custom CSS for better card visuals
st.markdown("""
    <style>
    .cert-card {
        border: 1px solid #e6e9ef;
        border-radius: 10px;
        padding: 20px;
        background-color: #f8f9fa;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📜 Professional Credentials & Academic Records")
st.write("Explore my verified certificates and academic background in Data Science and Business.")

# Database of certificates based on your files
certificates = [
    {"title": "Master in Data Science", "file": "Certificate - GUILHERME OYAKAWA DE ALMEIDA.jpg", "issuer": "Rome Business School", "category": "Academic"},
    {"title": "Power BI Data Analyst", "file": "DataCampCertification_PBI.jpg", "issuer": "DataCamp", "category": "Data BI"},
    {"title": "SQL Data Analyst", "file": "DataCampCertification_SQL.jpg", "issuer": "DataCamp", "category": "SQL"},
    {"title": "Python Data Analyst", "file": "certificate_python Data Analyst.jpg", "issuer": "DataCamp", "category": "Python"},
    {"title": "Academic Transcript", "file": "Transcript - Guilherme Oyakawa De Almeida.jpg", "issuer": "Rome Business School", "category": "Academic"},
]

# Filters
categories = ["All"] + sorted(list(set(c["category"] for c in certificates)))
selected_category = st.sidebar.selectbox("Filter by Category:", categories)

# Filtered list
filtered_certs = [c for c in certificates if selected_category == "All" or c["category"] == selected_category]

# Display in a grid
cols = st.columns(2) # Two columns for better visibility of details

for i, cert in enumerate(filtered_certs):
    with cols[i % 2]:
        st.markdown(f"""<div class="cert-card">
            <h3>{cert['title']}</h3>
            <p><b>Issuer:</b> {cert['issuer']} | <b>Category:</b> {cert['category']}</p>
        </div>""", unsafe_allow_html=True)
        
        st.image(cert["file"], use_container_width=True)
        
        with open(cert["file"], "rb") as f:
            st.download_button(
                label=f"⬇️ Download {cert['title']}",
                data=f,
                file_name=cert["file"],
                mime="image/jpeg",
                key=f"btn_{i}"
            )
        st.divider()
