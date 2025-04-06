def calculate_match_score(jd_skills, resume_skills):
    match = set(jd_skills).intersection(set(resume_skills))
    score = (len(match) / len(jd_skills)) * 100 if jd_skills else 0
    return round(score, 2)
