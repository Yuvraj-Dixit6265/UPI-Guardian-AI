from fastapi import APIRouter

router = APIRouter(
    prefix="/ai",
    tags=["AI Reliability"]
)


@router.get("/outage-prediction")
def outage_prediction():

    return {
        "message": "AI module under development"
    }