def simulate_region_failure(
    active_region,
    backup_region,
    requests_per_minute
):

    failover_time_seconds = 15

    increased_latency_ms = 250

    affected_customers = int(
        requests_per_minute * 0.20
    )

    return {
        "failed_region": active_region,
        "traffic_shifted_to": backup_region,
        "failover_time_seconds": failover_time_seconds,
        "estimated_latency_ms": increased_latency_ms,
        "affected_customers": affected_customers
    }