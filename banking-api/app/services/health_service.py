from sqlalchemy import text
from app.database import SessionLocal
import redis


def get_health_status():

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
        "database": db_status,
        "redis": redis_status
    }