import os
from utils.jd_agent import extract_jd_keywords
from utils.resume_agent import extract_resume_data
from utils.match_agent import calculate_match_score
from utils.email_agent import send_email

def main():
    # Load Job Description
    with open("jd_sample.txt", "r", encoding='utf-8') as f:
        jd_text = f.read()

    jd_keywords = extract_jd_keywords(jd_text)

    # Load resumes
    resume_folder = "resumes"
    for file in os.listdir(resume_folder):
        if file.endswith(".txt"):
            resume_path = os.path.join(resume_folder, file)
            with open(resume_path, "r", encoding='utf-8') as f:
                resume_text = f.read()

            resume_data = extract_resume_data(resume_text)
            score = calculate_match_score(jd_keywords, resume_data)

            print(f"\nFile: {file}")
            print(f"Match Score: {score:.2f}%")

            if score >= 80:
                print("Shortlisted ✅")
                send_email(resume_data["Name"])
            else:
                print("Not Shortlisted ❌")

if __name__ == "__main__":
    main()
