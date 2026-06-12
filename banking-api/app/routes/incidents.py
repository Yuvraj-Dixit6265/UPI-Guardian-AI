from fastapi import APIRouter

from app.services.incident_commander import (
    generate_incident_report
)

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.get("/latest")
def latest_incident():

    return generate_incident_report(
        risk="LOW",
        health_score=100,
        affected_customers=10
    )   