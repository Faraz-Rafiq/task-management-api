from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.modules.tasks.service import task_service
from app.modules.tasks.schema import (
    TaskCreate, TaskUpdate,
    TaskResponse, TaskListResponse
)
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.model import User

router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.create_task(db, task_data, current_user.id)

@router.get("/", response_model=TaskListResponse)
def get_tasks(
    status: str = Query(None),
    priority: str = Query(None),
    skip: int = Query(0),
    limit: int = Query(20),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.get_all_tasks(
        db, current_user.id, status, priority, skip, limit
    )

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.get_task(db, task_id, current_user.id)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    update_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.update_task(db, task_id, update_data, current_user.id)

@router.delete("/{task_id}", status_code=200)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.delete_task(db, task_id, current_user.id)