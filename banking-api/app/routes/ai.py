from fastapi import APIRouter

from app.services.ai_predictor import (
    predict_outage
)

router = APIRouter(
    prefix="/ai",
    tags=["AI Reliability"]
)


@router.get("/outage-prediction")
def outage_prediction():

    return predict_outage(
        latency=320,
        error_rate=8,
        healthy_regions=2
    )