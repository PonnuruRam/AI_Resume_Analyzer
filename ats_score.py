def calculate_ats_score(text):
    keywords = ["Python", "Java", "MySQL", "Git", "HTML", "CSS", "DBMS"]

    score = 0
    found = []

    for keyword in keywords:
        if keyword.lower() in text.lower():
            score += 100 / len(keywords)
            found.append(keyword)

    return round(score), found