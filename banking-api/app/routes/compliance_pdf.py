from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.compliance_service import (
    generate_compliance_report
)

from app.services.pdf_report_service import (
    generate_pdf_report
)

router = APIRouter(
    prefix="/compliance",
    tags=["Compliance PDF"]
)


@router.get("/pdf")
def generate_pdf():

    report_data = (
        generate_compliance_report()
    )

    pdf_path = (
        generate_pdf_report(report_data)
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=(
            "RBI_Operational_Resilience_Report.pdf"
        )
    )