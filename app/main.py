from fastapi import FastAPI
from app.core.config import settings
from app.modules.tasks.router import router as task_router
from app.modules.auth.router import router as auth_router

from app.core.logging import setup_logging, logger

# add inside the file after app = FastAPI(...)
setup_logging()
logger.info("Task Management API starting up")

app = FastAPI(title="Task Management API", version="0.1.0")

app.include_router(auth_router)
app.include_router(task_router)
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
