# Incident Response Playbook

## Severity Levels

### SEV-1

Full platform outage.

Actions:

1. Declare incident.
2. Notify stakeholders.
3. Restore service immediately.
4. Perform root cause analysis.

---

### SEV-2

Partial outage.

Actions:

1. Identify affected service.
2. Route traffic if possible.
3. Restore degraded functionality.
4. Monitor recovery.

---

### SEV-3

Performance degradation.

Actions:

1. Review Grafana dashboards.
2. Review Prometheus metrics.
3. Check infrastructure resources.
4. Optimize performance.

---

## Database Failure

1. Validate PostgreSQL availability.
2. Verify database connectivity.
3. Check Kubernetes pod health.
4. Restore service.

---

## Regional Failure

1. Mark region unhealthy.
2. Shift traffic.
3. Verify application health.
4. Restore failed region.

---

## High Error Rate

1. Review alerts.
2. Identify affected service.
3. Roll back deployment if required.
4. Monitor recovery.
