from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="Task Management API",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/v1/version")
def get_version():
    return {
        "app": "task-api",
        "version": "0.1.0",
        "environment": settings.ENVIRONMENT
    }