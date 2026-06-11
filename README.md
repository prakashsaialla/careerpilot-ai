# 🚀 CareerPilot AI

### Intelligent Career Guidance Platform Powered by Azure AI

CareerPilot AI is an AI-powered career coaching platform built for the Microsoft Agents League Hackathon 2026.

The platform helps students, graduates and job seekers evaluate their career readiness, improve resumes, prepare for interviews, identify skill gaps and generate personalized career roadmaps using Azure AI.

---

## 🌟 Features

### 🤖 Career Assessment Agent

* Career Readiness Score
* Resume Strength Analysis
* Weakness Detection
* Skill Gap Identification
* Learning Recommendations
* Certification Suggestions
* Interview Preparation
* Personalized Career Advice

### 📄 Resume Review

* ATS Optimization Suggestions
* Resume Quality Assessment
* Missing Skills Detection
* Improvement Recommendations

### 🎤 Interview Preparation

* Technical Questions
* Behavioral Questions
* Suggested Answers

### 🎯 Skill Gap Analysis

* Current Skills Assessment
* Target Role Comparison
* Missing Skills Identification
* Learning Roadmap Generation

### 📊 Resume Job Match

* Resume vs Job Description Comparison
* Match Percentage
* Missing Skills Analysis
* Hiring Readiness Insights

### 🗺️ Career Roadmap Generator

* Personalized Learning Plan
* Recommended Projects
* Certifications Path
* Career Growth Timeline

---

## 🏗️ Architecture

User
↓
CareerPilot AI (Streamlit)
↓
Azure OpenAI (gpt-oss-120b)
↓
AI Career Agents
↓
Career Recommendations

Fallback Provider:
Ollama (Local LLM)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Azure AI Foundry
* Azure OpenAI
* Ollama
* GitHub Copilot

---

## 🎯 Microsoft Agents League Alignment

CareerPilot AI demonstrates:

* AI Agent Workflows
* Multi-Step Career Reasoning
* Personalized Recommendations
* Resume Intelligence
* Career Planning Automation
* Azure AI Integration

The solution transforms traditional career guidance into an intelligent AI agent experience.

---

## 🚀 Getting Started

### Clone Repository

git clone <your-repo-url>

cd careerpilot-ai

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

AZURE_OPENAI_ENDPOINT=YOUR_ENDPOINT

AZURE_OPENAI_API_KEY=YOUR_KEY

AZURE_OPENAI_API_VERSION=YOUR_VERSION

### Run Application

streamlit run app.py

---

## ☁️ Deployment

### Streamlit Community Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add Azure secrets
4. Deploy

### Azure App Service

1. Create Azure Web App
2. Connect GitHub repository
3. Configure environment variables
4. Deploy

---

## 📷 Demo

<img width="1867" height="972" alt="image" src="https://github.com/user-attachments/assets/227eb390-2bd7-4b4e-bbe4-9778b4966133" />

---

## 👨‍💻 Built For

Microsoft Agents League Hackathon 2026

---

## 📄 License

MIT License
