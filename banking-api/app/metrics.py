from prometheus_client import Counter
from prometheus_client import Counter, Histogram
from prometheus_client import Gauge

accounts_created = Counter(
    "accounts_created_total",
    "Total accounts created"
)

deposits_total = Counter(
    "deposits_total",
    "Total successful deposits"
)

withdrawals_total = Counter(
    "withdrawals_total",
    "Total successful withdrawals"
)

transfers_total = Counter(
    "transfers_total",
    "Total successful transfers"
)

api_requests_total = Counter(
    "api_requests_total",
    "Total API Requests"
)

api_request_latency_seconds = Histogram(
    "api_request_latency_seconds",
    "API Request Latency"
)

api_errors_total = Counter(
    "api_errors_total",
    "Total API Errors"
)

current_health_score = Gauge(
    "current_health_score",
    "Current platform health score"
)