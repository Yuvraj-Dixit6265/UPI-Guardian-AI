from fastapi import APIRouter

from app.services.region_manager import (
    RegionManager
)

router = APIRouter(
    prefix="/multi-region",
    tags=["Multi Region"]
)

manager = RegionManager()


@router.get("/status")
def status():

    return manager.get_regions()


@router.post("/fail/{region}")
def fail_region(region: str):

    manager.mark_region_down(region)

    return {
        "healthy_regions":
        manager.failover()
    }
@router.get("/route")
def route_request():

    return {
        "selected_region":
        manager.get_best_region()
    }