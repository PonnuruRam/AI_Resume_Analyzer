from skills import skills

def extract_skills(text):
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills