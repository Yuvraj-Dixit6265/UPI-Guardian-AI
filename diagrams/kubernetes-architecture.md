# Kubernetes Architecture

```mermaid
flowchart TD

    Ingress --> Service

    Service --> Pod1[FastAPI Pod 1]
    Service --> Pod2[FastAPI Pod 2]
    Service --> Pod3[FastAPI Pod 3]

    Pod1 --> PostgreSQL
    Pod2 --> PostgreSQL
    Pod3 --> PostgreSQL

    HPA --> Service

    ConfigMap --> Pod1
    ConfigMap --> Pod2
    ConfigMap --> Pod3

    Secret --> Pod1
    Secret --> Pod2
    Secret --> Pod3
```
