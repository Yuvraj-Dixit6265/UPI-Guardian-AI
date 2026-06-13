# Monitoring Architecture

```mermaid
flowchart TD

    FastAPI --> Metrics

    Metrics --> Prometheus

    Prometheus --> Grafana

    Prometheus --> Alertmanager

    Alertmanager --> Email[Notifications]

    Grafana --> Dashboards
```
