# 🚀 Radiant AI: Your Agentic Career Co-Pilot

Turn your dream job into a step-by-step execution plan. Radiant AI is an agentic system that actively manages a student’s professional growth by analyzing their current profile, identifying market-driven skill gaps, and generating an adaptive 30-day roadmap.

## 🎯 The Vision
Students are overwhelmed by generic advice. Job roles evolve faster than traditional curricula. This is not a chatbot; it is a multi-step reasoning agent that acts as your personal career co-pilot.

## ⚙️ Core Features
* **Skill Extraction:** Parses resumes (PDF) and extracts structured skills using Hugging Face NLP models.
* **Market Alignment:** Maps real-world job requirements to your missing competencies using Kaggle dataset architectures and O*NET.
* **Agentic Planning:** Generates a personalized, gamified 30-day "Vibe-Check" learning roadmap.
* **Actionable Dashboard:** Tracks progress, calculates market value increase, and curates daily checkpoints.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI
* **Frontend:** HTML, Vanilla JS, Tailwind CSS
* **AI/Data:** Hugging Face (Token Classification), Kaggle Datasets, PyPDF2

## 🚀 How to Run Locally
1. Clone the repo.
2. Navigate to the `backend` directory: `cd backend`
3. Install dependencies: `pip install -r requirements.txt`
4. Add your Hugging Face API key to a `.env` file: `HF_TOKEN=your_token_here`
5. Run the server: `uvicorn main:app --reload`
6. Open `frontend/index.html` in your browser.
