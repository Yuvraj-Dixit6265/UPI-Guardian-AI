def calculate_risk_score(
    database_status,
    redis_status,
    error_count,
    avg_latency_ms
):

    score = 100

    if database_status == "DOWN":
        score -= 50

    if redis_status == "DOWN":
        score -= 20

    if error_count > 10:
        score -= 10

    if avg_latency_ms > 100:
        score -= 10

    if avg_latency_ms > 500:
        score -= 20

    score = max(score, 0)

    if score >= 80:
        risk = "LOW"

    elif score >= 50:
        risk = "MEDIUM"

    else:
        risk = "HIGH"

    return score, risk