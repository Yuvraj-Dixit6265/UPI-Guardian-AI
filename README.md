# UPI Guardian AI

AI-Powered Banking Reliability, Multi-Region Resilience, Monitoring, and Incident Management Platform.

---

## Overview

UPI Guardian AI is a reliability-focused banking platform designed to simulate enterprise-grade operational excellence practices used in modern fintech systems.

The platform combines:

* Banking APIs
* Kubernetes Orchestration
* Multi-Region Routing
* Disaster Recovery
* Monitoring and Alerting
* AI-Based Outage Prediction
* CI/CD Automation

---

## Features

### Banking Services

* Account Management
* Deposits
* Withdrawals
* Transfers
* Transaction History

### Reliability Engineering

* Health Monitoring
* Risk Assessment
* Incident Management
* Disaster Recovery Simulation

### Multi-Region Architecture

* Region A
* Region B
* Active-Active Routing
* Regional Failover

### Observability

* Prometheus
* Grafana
* Alertmanager

### AI Reliability Layer

Predicts:

* Outage Probability
* Customer Impact
* Recommended Actions

### DevOps

* Docker
* Kubernetes
* Horizontal Pod Autoscaler
* GitHub Actions CI/CD

---

## Architecture

### System Architecture

See:

```text
diagrams/system-architecture.md
```

### Kubernetes Architecture

See:

```text
diagrams/kubernetes-architecture.md
```

### Monitoring Architecture

See:

```text
diagrams/monitoring-architecture.md
```

### Multi-Region Architecture

See:

```text
diagrams/multi-region-architecture.md
```

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL

### Infrastructure

* Docker
* Kubernetes

### Monitoring

* Prometheus
* Grafana
* Alertmanager

### CI/CD

* GitHub Actions

### AI

* Python
* Rule-Based Reliability Engine

---

## API Endpoints

### Health

```http
GET /health/
```

### Risk Assessment

```http
GET /risk/
```

### Disaster Recovery

```http
GET /dr/simulate
```

### Incident Management

```http
GET /incidents/latest
```

### Multi Region

```http
GET /multi-region/status
GET /multi-region/route
POST /multi-region/fail/{region}
```

### AI Reliability

```http
GET /ai/outage-prediction
```

---

## Monitoring Stack

### Prometheus

Metrics collection and monitoring.

### Grafana

Operational dashboards and visualization.

### Alertmanager

Alert routing and incident notifications.

---

## Kubernetes Components

* Deployment
* Service
* ConfigMap
* Secret
* HPA
* Ingress

---

## SRE Documentation

See:

```text
docs/SLOs.md
docs/Error_Budget.md
docs/Incident_Playbook.md
```

---

## CI/CD Pipeline

Git Push

↓

Automated Validation

↓

Docker Build

↓

Docker Push

↓

Deployment Stage

---

## Screenshots

The following screenshots are available in the evidence folder:

* Swagger UI
* Kubernetes Pods
* Prometheus
* Grafana
* Alertmanager
* AI Reliability Endpoint
* Multi Region Routing
* GitHub Actions Pipeline

---

## Future Improvements

* Machine Learning-Based Outage Prediction
* Real Multi-Region Replication
* Chaos Engineering
* Canary Deployments
* Blue-Green Deployments

---

## Author

Yuvraj Krishna Dixit
