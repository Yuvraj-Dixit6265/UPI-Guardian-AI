from fastapi import APIRouter

from app.services.compliance_service import (
    generate_compliance_report
)

router = APIRouter(
    prefix="/compliance",
    tags=["Compliance"]
)


@router.get("/report")
def compliance_report():

    return generate_compliance_report()