# System Architecture

```mermaid
flowchart TD

    User[Client]

    User --> API[FastAPI API]

    API --> DB[(PostgreSQL)]

    API --> Redis[(Redis)]

    API --> AI[AI Reliability Engine]

    AI --> Region[Multi Region Manager]

    API --> Metrics[Prometheus Metrics]

    Metrics --> Prometheus

    Prometheus --> Grafana

    Prometheus --> Alertmanager
```
