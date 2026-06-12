def calculate_health_score(
    database_status,
    redis_status,
    error_count=0
):

    score = 100

    if database_status == "DOWN":
        score -= 50

    if redis_status == "DOWN":
        score -= 20

    if error_count > 10:
        score -= 10

    if score >= 80:
        risk = "LOW"

    elif score >= 50:
        risk = "MEDIUM"

    else:
        risk = "HIGH"

    return {
        "health_score": score,
        "risk": risk
    }