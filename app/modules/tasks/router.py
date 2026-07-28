from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.modules.tasks.service import task_service
from app.modules.tasks.schema import (
    TaskCreate, TaskUpdate, 
    TaskResponse, TaskListResponse
)

router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task_data)

@router.get("/", response_model=TaskListResponse)
def get_tasks(
    status: str = Query(None),
    priority: str = Query(None),
    skip: int = Query(0),
    limit: int = Query(20),
    db: Session = Depends(get_db)
):
    return task_service.get_all_tasks(db, status, priority, skip, limit)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return task_service.get_task(db, task_id)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, update_data: TaskUpdate, 
                db: Session = Depends(get_db)):
    return task_service.update_task(db, task_id, update_data)

@router.delete("/{task_id}", status_code=200)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_service.delete_task(db, task_id)