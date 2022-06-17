from flask import request
from prometheus_client import Counter, Histogram
import time

REQUEST_DURATION = Histogram('request_duration', 'Request duration',
    ['path','method', 'http_status']
)

def start_timer():
    request.start_time = time.time()

def stop_timer(response):
    resp_time = time.time() - request.start_time
    REQUEST_DURATION.labels(request.path, request.method, response.status_code).observe(resp_time)
    return response

def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(stop_timer)