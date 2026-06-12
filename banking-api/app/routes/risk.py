from fastapi import APIRouter

from app.services.health_service import get_health_status
from app.services.customer_impact_service import (
    predict_customer_impact
)

router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)


@router.get("/")
def get_risk():

    status = get_health_status()

    database_status = status["database"]
    redis_status = status["redis"]

    score = 100

    if database_status == "DOWN":
        score -= 50

    if redis_status == "DOWN":
        score -= 20

    if score >= 80:
        risk = "LOW"

    elif score >= 50:
        risk = "MEDIUM"

    else:
        risk = "HIGH"

    requests_per_minute = 1000

    affected_customers = predict_customer_impact(
        risk,
        requests_per_minute
    )

    return {
        "health_score": score,
        "risk": risk,
        "predicted_affected_customers": affected_customers
    }