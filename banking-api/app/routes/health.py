from fastapi import APIRouter
from sqlalchemy import text
from app.services.health_service import get_health_status
from app.database import SessionLocal
import redis

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
def health_check():

    db_status = "UP"
    redis_status = "UP"

    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()

    except Exception:
        db_status = "DOWN"

    try:
        redis_client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

        redis_client.ping()

    except Exception:
        redis_status = "DOWN"

    return {
        "service": "UP",
        "database": db_status,
        "redis": redis_status
    }
@router.get("/")
def health_check():

    status = get_health_status()

    return {
        "service": "UP",
        **status
    }