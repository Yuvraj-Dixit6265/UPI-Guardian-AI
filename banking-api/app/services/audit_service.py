import uuid

from app.database import SessionLocal
from app.models import AuditEvent


def log_event(
    event_type,
    status,
    details=""
):

    db = SessionLocal()

    event = AuditEvent(
        event_id=str(uuid.uuid4()),
        event_type=event_type,
        status=status,
        details=details
    )

    db.add(event)
    db.commit()
    db.close()