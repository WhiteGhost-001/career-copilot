from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import our custom AI tools from the utils folder (we will make these next!)
from utils.extractor import extract_text_from_pdf
from utils.hf_api import extract_skills
from utils.agent import generate_30_day_plan

app = FastAPI(title="Radiant AI - Career Co-Pilot API")

# Allow the separated frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For hackathon purposes. In prod, we restrict this.
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {"status": "Radiant AI Agent Backend is Online"}

@app.post("/api/generate-roadmap")
async def generate_roadmap(
    dream_role: str = Form(...),
    current_status: str = Form(...),
    resume: UploadFile = File(...)
):
    print(f"Agent Initialized for Role: {dream_role}")
    
    # Step 1: Read the PDF
    if not resume.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported right now.")
    
    file_bytes = await resume.read()
    raw_text = extract_text_from_pdf(file_bytes)
    
    if not raw_text:
        raise HTTPException(status_code=400, detail="Failed to extract text from PDF.")

    # Step 2: Extract Skills via Hugging Face
    print("Extracting skills via Hugging Face...")
    user_skills = extract_skills(raw_text)
    print(f"Skills found: {user_skills}")

    # Step 3: Agent Reasoning & Roadmap Generation
    print("Agent is mapping market data and planning...")
    roadmap_data = generate_30_day_plan(dream_role, user_skills)

    # Combine inputs with the generated plan
    response_data = {
        "status": "success",
        "role_analyzed": dream_role,
        "current_status": current_status,
        "data": roadmap_data
    }
    
    return response_data

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
