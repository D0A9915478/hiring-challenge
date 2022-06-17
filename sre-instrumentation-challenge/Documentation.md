### middleware.py

Defines the prometheus metric as a histogram so we can observe the request duration, with additional labels as specified.
Contains code for calculating request duration, with a timer starting before a request, then stopping after.

### bucket.py

Prometheus exposed under route /metrics/

### Dockerfile

Dependency installation handled the same way documentation specifies, as such setup.py modified to include prometheus_client

### docker compose

Container name set as prometheus expects it with port 5000 exposed

### k8s manifests

Generated with kompose convert

### Grafana visualisation

Average request duration

```
sum(rate(request_duration_sum[5m])) / sum(rate(request_duration_count[5m]))
```

Status codes:

```
count by (http_status)(request_duration_created)
```