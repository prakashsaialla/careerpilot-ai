import streamlit as st
import requests
from pypdf import PdfReader

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# UI Header
# -----------------------------
st.title("🚀 CareerPilot AI")

st.markdown("""
### Your Personal AI Career Coach

Features:
- 📄 Resume Review
- 🎤 Interview Preparation
- 🎯 Skill Gap Analysis
- 📊 Resume Job Match
- 🗺️ Career Roadmap
- 💬 Career Guidance
""")

# -----------------------------
# Helper Functions
# -----------------------------
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text


def generate_ai_response(prompt):
    with st.spinner("Analyzing..."):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False
            }
        )

    st.success("Analysis Complete!")
    return response.json()["response"]


# -----------------------------
# Sidebar Navigation
# -----------------------------
page = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Dashboard",
        "Career Chat",
        "Resume Review",
        "Interview Prep",
        "Skill Gap Analysis",
        "Resume Job Match",
        "Career Roadmap"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------
if page == "Dashboard":

    st.header("🚀 Welcome to CareerPilot AI")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📄 Resume Review")

    with col2:
        st.info("🎤 Interview Preparation")

    col3, col4 = st.columns(2)

    with col3:
        st.info("🎯 Skill Gap Analysis")

    with col4:
        st.info("📊 Resume Job Match")

    st.success(
        "Your AI-powered career coach for students and job seekers."
    )

# -----------------------------
# Career Chat
# -----------------------------
elif page == "Career Chat":

    st.header("💬 Career Chat")

    prompt = st.text_area("Ask a career question")

    if st.button("Generate Response"):

        result = generate_ai_response(prompt)
        st.write(result)

# -----------------------------
# Resume Review
# -----------------------------
elif page == "Resume Review":

    st.header("📄 Resume Review")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:

        resume_text = extract_text(uploaded_file)

        st.success("Resume uploaded successfully!")

        st.text_area(
            "Resume Content",
            resume_text,
            height=250
        )

        if st.button("Analyze Resume"):

            prompt = f"""
You are an expert career coach and ATS reviewer.

Analyze this resume and provide:

# Resume Score
Give a score out of 10.

# Strengths
List the strongest aspects.

# Weaknesses
List improvement areas.

# Missing Skills
Identify important missing skills.

# ATS Optimization
Suggest ATS improvements.

# Final Recommendations
Provide 3 actionable improvements.

Resume:

{resume_text}
"""

            result = generate_ai_response(prompt)

            st.subheader("AI Resume Analysis")
            st.write(result)

# -----------------------------
# Interview Prep
# -----------------------------
elif page == "Interview Prep":

    st.header("🎤 Interview Preparation")

    role = st.text_input("Enter Target Job Role")

    if st.button("Generate Interview Questions"):

        prompt = f"""
Generate:

- 10 technical interview questions
- 10 behavioral interview questions
- Suggested answers

For the role:

{role}
"""

        result = generate_ai_response(prompt)

        st.write(result)

# -----------------------------
# Skill Gap Analysis
# -----------------------------
elif page == "Skill Gap Analysis":

    st.header("🎯 Skill Gap Analysis")

    current_skills = st.text_area(
        "Enter Your Current Skills"
    )

    target_role = st.text_input(
        "Target Role"
    )

    if st.button("Analyze Skill Gap"):

        prompt = f"""
You are an AI career advisor.

Current Skills:
{current_skills}

Target Role:
{target_role}

Provide:

# Skill Match Analysis

# Missing Skills

# Recommended Certifications

# Learning Roadmap

# Estimated Timeline

# Career Advice
"""

        result = generate_ai_response(prompt)

        st.subheader("Skill Gap Report")
        st.write(result)

# -----------------------------
# Resume Job Match
# -----------------------------
elif page == "Resume Job Match":

    st.header("📊 Resume vs Job Match")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Paste Job Description"
    )

    if uploaded_file and job_description:

        resume_text = extract_text(uploaded_file)

        if st.button("Analyze Match"):

            prompt = f"""
Compare this resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:

1. Match Score (0-100)
2. Matching Skills
3. Missing Skills
4. Recommended Improvements
5. Hiring Chances
"""

            result = generate_ai_response(prompt)

            st.write(result)

# -----------------------------
# Career Roadmap
# -----------------------------
elif page == "Career Roadmap":

    st.header("🗺️ Career Roadmap Generator")

    current_role = st.text_input(
        "Current Role"
    )

    target_role = st.text_input(
        "Target Career Goal"
    )

    if st.button("Generate Roadmap"):

        prompt = f"""
Create a detailed career roadmap.

Current Role:
{current_role}

Target Role:
{target_role}

Provide:

1. Skills to Learn
2. Certifications
3. Projects to Build
4. Learning Timeline
5. Job Search Strategy
"""

        result = generate_ai_response(prompt)

        st.write(result)
