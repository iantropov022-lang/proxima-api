from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="Proxima API",
    description="Mini FastAPI service for proxima-regul.ru",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "proxima-api",
        "domain": "proxima-regul.ru",
        "status": "running",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/healthz")
def healthz():
    return {
        "status": "ok",
    }