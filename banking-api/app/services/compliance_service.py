from app.database import SessionLocal
from app.models import AuditEvent


def generate_compliance_report():

    db = SessionLocal()

    total_failovers = db.query(AuditEvent)\
        .filter(
            AuditEvent.event_type == "FAILOVER"
        ).count()

    total_incidents = db.query(AuditEvent)\
        .filter(
            AuditEvent.event_type == "INCIDENT"
        ).count()

    db.close()

    # Simulated operational resilience metrics
    availability_percentage = 99.95
    health_score = 100
    rto_seconds = 15
    rpo_seconds = 0

    observation = None

    if (
        availability_percentage < 99.5
        or rto_seconds > 60
        or total_incidents > 3
    ):
        compliance_status = "NON_COMPLIANT"

        observation = (
            "Critical operational resilience "
            "thresholds exceeded."
        )

    elif (
        availability_percentage < 99.95
        or total_incidents > 1
        or rto_seconds > 15
    ):
        compliance_status = "COMPLIANT_WITH_OBSERVATIONS"

        observation = (
            "Minor operational deviations detected. "
            "Review and remediation recommended."
        )

    else:
        compliance_status = "COMPLIANT"

        observation = (
            "All operational resilience controls "
            "are within acceptable limits."
        )

    report = {
        "availability_percentage": availability_percentage,
        "total_incidents": total_incidents,
        "total_failovers": total_failovers,
        "health_score": health_score,
        "risk_level": "LOW",
        "rto_seconds": rto_seconds,
        "rpo_seconds": rpo_seconds,
        "compliance_status": compliance_status,
        "observation": observation
    }

    return report