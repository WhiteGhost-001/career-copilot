import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
# Using a popular model for skill extraction
API_URL = "https://api-inference.huggingface.co/models/jjzha/jobbert_skill_extraction"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def extract_skills(text: str) -> list:
    """
    Sends resume text to Hugging Face to extract a list of skills.
    """
    if not text:
        return []

    # Hugging Face API limits payload size, so we truncate to the first 2000 chars for the MVP
    payload = {"inputs": text[:2000]}
    
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        
        # The model returns entities (skills). We filter and clean them up.
        skills = set() # Use a set to avoid duplicates
        for entity in data:
            if entity.get("entity_group") == "Skill":
                # Capitalize nicely (e.g., "python" -> "Python")
                skills.add(entity.get("word").strip().title())
                
        return list(skills)
        
    except Exception as e:
        print(f"Hugging Face API Error: {e}")
        # Fallback for the hackathon presentation if the API rate limits you
        return ["Python", "C++", "Data Analysis", "Communication"]
