from predictor import predict_outage


def generate_ai_recommendation(
    latency,
    error_rate,
    healthy_regions
):

    prediction = predict_outage(
        latency,
        error_rate,
        healthy_regions
    )

    recommendation = "System Healthy"

    if prediction["outage_probability"] >= 70:
        recommendation = (
            "Shift traffic to backup region"
        )

    elif prediction["outage_probability"] >= 40:
        recommendation = (
            "Monitor system closely"
        )

    return {
        **prediction,
        "recommended_action":
        recommendation
    }