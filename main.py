import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# UI
st.set_page_config(page_title="Resume Analyzer")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze this resume and provide:

1. ATS Score out of 100
2. Skills Found
3. Missing Skills
4. Strengths
5. Weaknesses
6. Suggestions for Improvement
7. Suitable Job Roles

Resume:

{resume_text}
"""

        response = model.generate_content(prompt)

        st.subheader("Analysis")

        st.write(response.text)