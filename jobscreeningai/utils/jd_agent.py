def extract_jd_keywords(jd_text):
    lines = jd_text.lower().split("\n")
    skills = []
    for line in lines:
        if "skills" in line or "experience" in line:
            skills += [word.strip() for word in line.split(":")[1].split(",")]
    return skills
