import streamlit as st
from pdf_extractor import extract_text_from_pdf
from ai_analyzer import analyze_resume
import tempfile
import os

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 12px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {background-color: #45a049;}
    .header-box {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .upload-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-box">
        <h1>📄 AI Resume Analyzer</h1>
        <p style="font-size:18px; margin:0;">Get instant AI-powered feedback on your resume</p>
    </div>
""", unsafe_allow_html=True)

# 3 feature columns
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🎯 Smart Scoring\nGet an overall score out of 10")
with col2:
    st.markdown("### 🔍 Skill Analysis\nDiscover missing skills instantly")
with col3:
    st.markdown("### 💼 Job Matching\nFind your best fitting roles")

st.divider()

# Upload section
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
st.markdown("### 📁 Upload Your Resume")
uploaded_file = st.file_uploader("Supported format: PDF", type=["pdf"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    st.success(f"✅ **{uploaded_file.name}** uploaded successfully!")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("📖 Reading your resume..."):
        resume_text = extract_text_from_pdf(tmp_path)

    with st.expander("📃 View Extracted Text"):
        st.text(resume_text[:1000] + "...")

    st.markdown("###")
    if st.button("🔍 Analyze My Resume"):
        with st.spinner("🤖 AI is analyzing your resume... please wait"):
            result = analyze_resume(resume_text)

        st.markdown("---")
        st.markdown("## 📊 Analysis Results")
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(result)
        st.markdown('</div>', unsafe_allow_html=True)

        st.balloons()
        os.unlink(tmp_path)

st.divider()
st.markdown("""
    <div style='text-align:center; padding:10px;'>
        <span style='color:gray; font-size:14px;'>Built by </span>
        <span style='color:#667eea; font-size:20px; font-weight:bold;'>© Syed Farhad</span>
        <span style='color:gray; font-size:14px;'> using Streamlit + Groq AI (Llama 3.3)</span>
    </div>
""", unsafe_allow_html=True)