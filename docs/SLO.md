# Service Level Objectives (SLOs)

## API Availability

Target: 99.9%

Measurement:
Successful HTTP Requests / Total HTTP Requests

Monitoring:
Prometheus Metrics

Alert Threshold:
Availability below 99.9%

---

## API Latency

Target:
95% of requests below 300ms

Measurement:
Request Duration Metrics

Monitoring:
Prometheus + Grafana

Alert Threshold:
Latency above 300ms

---

## Database Availability

Target:
99.95%

Measurement:
Database Health Endpoint

Monitoring:
Health Checks

Alert Threshold:
Database Status DOWN

---

## Multi-Region Availability

Target:
100% successful traffic routing during regional failure

Measurement:
Region Health Checks

Monitoring:
Region Manager Service

Alert Threshold:
Less than one healthy region available
