import streamlit as st
from pdf_reader import read_pdf
from skill_extractor import extract_skills
from score import calculate_score
from ats_score import calculate_ats_score
from pdf_report import create_pdf
from database import save_data, view_data
import pandas as pd

st.title("Resume Analyzer")

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
    st.subheader("🎯 ATS Score")

    ats_score, found = calculate_ats_score(text)

    st.success(f"ATS Score: {ats_score}/100")
    st.subheader("Suggestions")

    if score < 40:
        st.write("Add more skills and projects.")

    elif score < 70:
        st.write("Good resume. Add certifications.")

    else:
         st.write("Excellent Resume!")
    st.subheader("Recommended Job Role")

    role = "General IT Professional"

    if "Python" in skills and "Machine Learning" in skills:
        role = "AI / Machine Learning Engineer"

    elif "Java" in skills:
        role = "Software Developer"

    elif "MySQL" in skills:
        role = "Database Developer"

    elif "HTML" in skills:
        role = "Web Developer"

    st.success(role)
    save_data(
        uploaded_file.name,
        score,
        ats_score,
        role
)
    st.subheader("📄 Download PDF Report")

    pdf_file = create_pdf(score, ats_score, skills, role)

    with open(pdf_file, "rb") as file:
        st.download_button(
        label="Download Report",
        data=file,
        file_name="Resume_Report.pdf",
        mime="application/pdf"
    )
        st.subheader("🗄️ Resume History")

        records = view_data()

        df = pd.DataFrame(
            records,
            columns=["ID", "File Name", "Resume Score", "ATS Score", "Role"]
   )

        st.dataframe(df)