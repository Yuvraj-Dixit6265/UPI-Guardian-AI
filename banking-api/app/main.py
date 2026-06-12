from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import generate_latest

from app.database import Base
from app.database import engine
from app.routes.compliance import (
    router as compliance_router
)
from app.routes.compliance_pdf import (
    router as compliance_pdf_router
)

import app.models

from app.middleware import MetricsMiddleware

from app.routes.accounts import router as accounts_router
from app.routes.transactions import router as transactions_router
from app.routes.health import router as health_router
from app.routes.risk import router as risk_router
from app.routes.disaster_recovery import router as dr_router
from app.routes.incidents import router as incidents_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="UPI Guardian Banking API"
)

app.add_middleware(MetricsMiddleware)

app.include_router(accounts_router)
app.include_router(transactions_router)
app.include_router(health_router)
app.include_router(risk_router)
app.include_router(dr_router)
app.include_router(incidents_router)
app.include_router(compliance_router)
app.include_router(
    compliance_pdf_router
)


@app.get("/")
def root():
    return {
        "message": "UPI Guardian API Running"
    }


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )