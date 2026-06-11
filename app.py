import streamlit as st
from openai import OpenAI
import requests
from pypdf import PdfReader
import re



azure_client = OpenAI(
    api_key="API_KEY",
    base_url="https://prakash-alla.openai.azure.com/openai/v1"
)


def load_css():
        with open("styles.css", "r", encoding="utf-8") as f:
            css = f.read()

        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True
        )


load_css()
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
}

div[data-testid="stMetric"] {
    background-color: #1e293b;
    border-radius: 12px;
    padding: 15px;
}

.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------
# UI Header
# -----------------------------
nav1, nav2, nav3, nav4, nav5, nav6, nav7, nav8 = st.columns(
    [1,1,1,1,1,1,1,1]
)


with nav1:
    if st.button("🏠 Home"):
        st.session_state.page = "Dashboard"

with nav2:
    if st.button("🤖 AI Agent"):
        st.session_state.page = "Career Assessment Agent"

with nav3:
    if st.button("📄 Resume Review"):
        st.session_state.page = "Resume Review"

with nav4:
    if st.button("🎤 Interview Prep"):
        st.session_state.page = "Interview Prep"

with nav5:
    if st.button("🎯 Skill Gap"):
        st.session_state.page = "Skill Gap Analysis"

with nav6:
    if st.button("📊 Job Match"):
        st.session_state.page = "Resume Job Match"

with nav7:
    if st.button("🗺️ Roadmap"):
        st.session_state.page = "Career Roadmap"

with nav8:
    ai_provider = st.selectbox(
        "",
        ["Azure AI", "Ollama"],
        label_visibility="collapsed"
    )

st.markdown(
    "<hr style='margin-top:5px;margin-bottom:10px;'>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
padding:20px;
border-radius:16px;
background: linear-gradient(135deg, #0078D4, #50E6FF);
text-align:center;
margin-bottom:15px;
">

<h1 style="
color:white;
margin-bottom:5px;
font-size:2.3rem;
">
🚀 CareerPilot AI
</h1>

<h4 style="
color:white;
margin-top:0;
margin-bottom:9px;
">
Your Intelligent Career Co-Pilot
</h4>

<p style="
color:white;
font-size:17px;
margin-bottom:0;
">
AI-powered career assessments, resume intelligence,
interview coaching, skill-gap analysis and personalized roadmaps.
</p>

</div>
""", unsafe_allow_html=True)

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


def generate_ollama_response(prompt):
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

def generate_azure_response(prompt):

    with st.spinner("Analyzing with Azure AI..."):

        response = azure_client.chat.completions.create(
            model="gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    return response.choices[0].message.content

def generate_ai_response(prompt):

    if ai_provider == "Azure AI":
        return generate_azure_response(prompt)

    else:
        return generate_ollama_response(prompt)


if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


page = st.session_state.page


# -----------------------------
# Dashboard
# -----------------------------


if page == "Dashboard":

    st.header("🚀 Welcome to CareerPilot AI")

    st.success(
        "AI-powered career guidance platform for students, graduates, and job seekers."
    )

    # Metrics Row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Provider",
            ai_provider
        )

    with col2:
        st.metric(
            "Features",
            "6+"
        )

    with col3:
        st.metric(
            "Career Analysis",
            "Ready"
        )

    st.divider()


    st.success(
        "Your AI-powered career coach for students and job seekers."
    )


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

    if role:

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

    if current_skills and target_role:

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

    if current_role and target_role:

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


#-----------------
#Career Assessment Page
#-----------------

elif page == "Career Assessment Agent":

    st.header("🤖 Career Assessment Agent")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    target_role = st.text_input(
        "Target Role"
    )

    if uploaded_file and target_role:

        if st.button("🚀 Analyze Me"):

            resume_text = extract_text(uploaded_file)

            prompt = f"""
                You are an expert AI Career Coach.

                Analyze the following resume for the target role.

                TARGET ROLE:
                {target_role}

                RESUME:
                {resume_text}

                Provide your response in the following format:

                # Career Readiness Score
                Analyze the resume against the target role and provide a realistic score from 0-100.

                Format:
                Career Readiness Score: XX

                Do NOT default to scores around 70-80.
                Give a genuinely calculated score based on:
                - skills match
                - experience match
                - projects
                - certifications
                - resume quality

                # Resume Strengths
                List the strongest aspects.

                # Resume Weaknesses
                List improvement areas.

                # Skill Gap Analysis
                Compare the candidate against the target role.

                # Missing Skills
                List missing technical and soft skills.

                # Learning Roadmap
                Provide a step-by-step roadmap.

                # Recommended Certifications
                Suggest relevant certifications.

                # Interview Preparation
                Generate:
                - 5 Technical Questions
                - 5 Behavioral Questions

                # Final Career Advice
                Provide personalized recommendations.
                """
            
            status = st.status(
                "🤖 CareerPilot AI Agent Working...",
                expanded=True
            )

            status.write("📄 Reading resume...")
            status.write("🎯 Understanding target role...")
            status.write("🔍 Identifying strengths and weaknesses...")
            status.write("📊 Calculating readiness score...")
            status.write("🧠 Generating recommendations...")
            

            result = generate_ai_response(prompt)

            result = re.sub(
                r"Career Readiness Score:\s*\d+\s*",
                "",
                result,
                re.IGNORECASE
            )


            status.update(
                label="✅ Assessment Complete",
                state="complete"
            )

            insight_prompt = f"""
            Based on this assessment, provide ONE short career insight.

            Maximum 20 words.

            Assessment:
            {result}
            """

            insight = generate_ai_response(insight_prompt)
            st.info(f"💡 Career Insight: {insight}")

            score_match = re.search(
                r"(\d{1,3})",
                result
            )

            score = 0

            if score_match:
                score = int(score_match.group(1))

            else:
                st.warning(
                    "Could not extract readiness score."
                )

            st.metric(
                "Career Readiness Score",
                f"{score}/100"
            )

            st.subheader("⚙️ Agent Workflow")

            c1, c2, c3, c4, c5 = st.columns(5)

            with c1:
                st.success("📄 Resume")

            with c2:
                st.success("🎯 Role")

            with c3:
                st.success("🧠 Analysis")

            with c4:
                st.success("📊 Scoring")

            with c5:
                st.success("🚀 Roadmap")

            if score >= 80:
                status = "Job Ready"
            elif score >= 60:
                status = "Almost Ready"
            else:
                status = "Needs Development"


            st.progress(score)

            st.subheader("🤖 Career Assessment Report")

            st.write(result)

            with st.expander("View Extracted Resume"):
                st.text_area(
                    "",
                    resume_text[:1000],
                    height=200
                )

            st.download_button(
                "📥 Download Report",
                result,
                file_name="career_report.txt"
            )


            st.divider()

            st.caption(
                "Built with Azure AI, Streamlit, Ollama and GitHub Copilot"
            )
