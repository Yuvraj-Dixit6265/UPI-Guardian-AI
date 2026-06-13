class RegionManager:

    def __init__(self):

        self.regions = {
            "Region-A": {
                "status": "HEALTHY",
                "latency": 120,
                "traffic_percentage": 50
            },
            "Region-B": {
                "status": "HEALTHY",
                "latency": 140,
                "traffic_percentage": 50
            }
        }

    def get_regions(self):
        return self.regions

    def mark_region_down(self, region):

        if region in self.regions:
            self.regions[region]["status"] = "DOWN"

    def failover(self):

        active_regions = [
            r
            for r, data in self.regions.items()
            if data["status"] == "HEALTHY"
        ]

        return active_regions
def get_best_region(self):

    healthy_regions = {
        name: data
        for name, data in self.regions.items()
        if data["status"] == "HEALTHY"
    }

    if not healthy_regions:
        return None

    return min(
        healthy_regions,
        key=lambda r:
        healthy_regions[r]["latency"]
    )