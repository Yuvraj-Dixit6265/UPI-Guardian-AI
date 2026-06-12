from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(report_data):

    pdf_path = (
        "reports/"
        "RBI_Operational_Resilience_Report.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "RBI Operational Resilience Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    for key, value in report_data.items():

        content.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 6)
        )

    doc.build(content)

    return pdf_path