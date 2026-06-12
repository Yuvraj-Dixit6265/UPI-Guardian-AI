def predict_customer_impact(
    risk_level: str,
    requests_per_minute: int
):

    if risk_level == "LOW":
        affected = int(requests_per_minute * 0.01)

    elif risk_level == "MEDIUM":
        affected = int(requests_per_minute * 0.10)

    else:
        affected = int(requests_per_minute * 0.30)

    return affected