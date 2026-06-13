def predict_outage(
    latency,
    error_rate,
    healthy_regions
):

    score = 0

    if latency > 500:
        score += 40

    elif latency > 250:
        score += 20

    if error_rate > 10:
        score += 40

    elif error_rate > 5:
        score += 20

    if healthy_regions < 2:
        score += 20

    score = min(score, 100)

    if score >= 70:
        impact = "HIGH"

    elif score >= 40:
        impact = "MEDIUM"

    else:
        impact = "LOW"

    recommendation = "System Healthy"

    if score >= 70:
        recommendation = "Shift traffic to backup region"

    elif score >= 40:
        recommendation = "Monitor system closely"

    return {
        "outage_probability": score,
        "customer_impact": impact,
        "recommended_action": recommendation
    }