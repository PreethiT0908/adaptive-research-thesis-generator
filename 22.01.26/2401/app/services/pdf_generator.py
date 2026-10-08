from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(thesis_draft, output_path):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()
    content = []

    for i, chapter in enumerate(thesis_draft.chapter_drafts):

        content.append(
            Paragraph(f"Chapter {i+1}: {chapter.chapter_title}", styles['Heading2'])
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(f"Objective: {chapter.objective}", styles['Normal'])
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(f"Draft: {chapter.draft}", styles['Normal'])
        )

        content.append(Spacer(1, 20))

    doc.build(content)
    return output_path