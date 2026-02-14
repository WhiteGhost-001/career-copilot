def generate_30_day_plan(dream_role: str, user_skills: list) -> dict:
    """
    Analyzes the gap between user skills and market requirements, 
    then generates a personalized learning plan.
    """
    # Mocking Kaggle/O*NET Data for MVP speed
    # In a real app, this would query a database of scraped job descriptions
    market_data = {
        "AI Engineer": ["Python", "TensorFlow", "PyTorch", "Linear Algebra", "FastAPI"],
        "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas"],
        "Frontend Developer": ["Html", "Css", "Javascript", "React", "Tailwind"],
        "Backend Developer": ["Python", "Django", "Node.Js", "Sql", "Docker"]
    }

    # Normalize the dream role to find the closest match
    required_skills = []
    for role, skills in market_data.items():
        if role.lower() in dream_role.lower():
            required_skills = skills
            break
    
    # Default fallback if the role isn't in our mock database
    if not required_skills:
        required_skills = ["Python", "Project Management", "Git", "Communication"]

    # Calculate the GAP
    missing_skills = [skill for skill in required_skills if skill not in user_skills]
    
    # Calculate Gamified Market Value (Base $10k per missing skill learned)
    value_increase = len(missing_skills) * 10000

    # Generate the dynamic roadmap based on missing skills
    roadmap = []
    day = 1
    
    # First, allocate days to missing skills
    for skill in missing_skills:
        roadmap.append({"day": day, "task": f"Phase 1: Deep Dive into {skill} basics.", "points": 100, "status": "pending"})
        day += 1
        roadmap.append({"day": day, "task": f"Phase 2: Build a mini-project using {skill}.", "points": 200, "status": "pending"})
        day += 1

    # Fill the rest of the 30 days with agentic tasks (Networking, LeetCode, etc.)
    filler_tasks = [
        "Update GitHub README with current progress.",
        "Connect with 3 professionals on LinkedIn in your target role.",
        "Solve 2 Data Structure & Algorithm problems.",
        "Read an industry research paper or Kaggle notebook.",
        "Refactor your recent code for better performance."
    ]
    
    filler_index = 0
    while day <= 30:
        roadmap.append({
            "day": day, 
            "task": filler_tasks[filler_index % len(filler_tasks)], 
            "points": 50, 
            "status": "pending"
        })
        day += 1
        filler_index += 1

    return {
        "user_skills_found": user_skills,
        "missing_skills": missing_skills,
        "market_value_increase": f"${value_increase:,}/yr",
        "roadmap": roadmap[:30] # Ensure exactly 30 days
    }
