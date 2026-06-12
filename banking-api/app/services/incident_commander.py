def generate_incident_report(
    risk,
    health_score,
    affected_customers
):

    if risk == "HIGH":

        severity = "HIGH"

        action = (
            "Immediate failover validation "
            "and traffic redistribution required."
        )

    elif risk == "MEDIUM":

        severity = "MEDIUM"

        action = (
            "Monitor latency and error rates."
        )

    else:

        severity = "LOW"

        action = (
            "No action required."
        )

    return {
        "severity": severity,
        "incident_summary": (
            f"Platform health score is "
            f"{health_score}."
        ),
        "predicted_customer_impact": affected_customers,
        "recommended_action": action
    }