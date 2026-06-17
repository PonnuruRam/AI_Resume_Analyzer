import streamlit as st
from pdf_reader import read_pdf
from skill_extractor import extract_skills
from score import calculate_score

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = read_pdf(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.subheader("Resume Content")
    st.write(text)

    skills = extract_skills(text)
    score = calculate_score(skills)
    st.subheader("Detected Skills")

    if skills:
        for skill in skills:
            st.write("✅", skill)
        st.write("Total Skills Found:", len(skills))
    else:
        st.write("No skills detected")
    st.subheader("Resume Score")
    st.progress(score)
    st.subheader("Suggestions")

    if score < 50:
        st.warning("Add more technical skills and certifications.")
    elif score < 80:
        st.info("Good resume. Add projects and internships.")
    else:
         st.success("Excellent resume! Your resume is strong.")
    st.write(score, "/100")
    st.subheader("Suggestions")

    if score < 40:
        st.write("Add more skills and projects.")

    elif score < 70:
        st.write("Good resume. Add certifications.")

    else:
         st.write("Excellent Resume!")
    st.subheader("Recommended Job Role")

    if "Python" in skills and "Machine Learning" in skills:
        st.success("AI / Machine Learning Engineer")

    elif "Java" in skills:
        st.success("Software Developer")

    elif "MySQL" in skills:
        st.success("Database Developer")

    elif "HTML" in skills:
        st.success("Web Developer")

    else:
        st.info("General IT Professional")