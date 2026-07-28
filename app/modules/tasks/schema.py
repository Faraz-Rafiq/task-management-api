from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.modules.tasks.model import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class TaskListResponse(BaseModel):
    tasks: list[TaskResponse]
    total: int