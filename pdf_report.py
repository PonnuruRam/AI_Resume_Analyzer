from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(score, ats_score, skills, role):

    pdf_file = "resume_report.pdf"

    doc = SimpleDocTemplate(pdf_file)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Resume Analyzer Report", styles['Title']))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"Resume Score: {score}/100", styles['Normal']))
    content.append(Paragraph(f"ATS Score: {ats_score}/100", styles['Normal']))
    content.append(Paragraph(f"Recommended Role: {role}", styles['Normal']))

    content.append(Spacer(1, 12))

    content.append(Paragraph("Detected Skills:", styles['Heading2']))

    for skill in skills:
        content.append(Paragraph(f"• {skill}", styles['Normal']))

    doc.build(content)

    return pdf_file