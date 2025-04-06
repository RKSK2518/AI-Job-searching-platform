def extract_resume_data(resume_text):
    lines = resume_text.lower().split("\n")
    skills = []
    for line in lines:
        if "skills" in line:
            skills += [word.strip() for word in line.split(":")[1].split(",")]
    return skills
