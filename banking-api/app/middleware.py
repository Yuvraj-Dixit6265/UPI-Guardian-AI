import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.metrics import (
    api_requests_total,
    api_request_latency_seconds,
    api_errors_total
)


class MetricsMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time()

        response = await call_next(request)

        duration = time.time() - start_time

        api_requests_total.inc()

        api_request_latency_seconds.observe(duration)

        if response.status_code >= 400:
            api_errors_total.inc()

        return response