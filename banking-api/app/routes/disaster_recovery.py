from fastapi import APIRouter
from app.services.audit_service import log_event

from app.services.region_simulator import (
    simulate_region_failure
)

router = APIRouter(
    prefix="/dr",
    tags=["Disaster Recovery"]
)


@router.get("/simulate")
def simulate():

    result = simulate_region_failure(
        active_region="Region-A",
        backup_region="Region-B",
        requests_per_minute=1000
    )

    log_event(
        event_type="FAILOVER",
        status="SUCCESS",
        details="Region-A traffic shifted to Region-B"
    )

    return result