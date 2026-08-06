from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.exceptions import AppException
from app.core.logging import setup_logging, logger

from app.modules.tasks.router import router as task_router
from app.modules.auth.router import router as auth_router

app = FastAPI(title="Task Management API", version="0.1.0")

setup_logging()
logger.info("Task Management API starting up")

app.include_router(auth_router)
app.include_router(task_router)


@app.exception_handler(AppException)
def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": exc.code, "message": exc.message}},
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