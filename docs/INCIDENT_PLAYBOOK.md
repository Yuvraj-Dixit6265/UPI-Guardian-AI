# Incident Response Playbook

## Application Down

1. Check Pods
2. Check Logs
3. Check PostgreSQL
4. Check Prometheus
5. Rollback Deployment

---

## Database Down

1. Verify postgres pod
2. Verify service
3. Check connection strings
4. Restore backup if needed

---

## High CPU

1. Verify HPA status
2. Scale deployment
3. Investigate traffic spikes