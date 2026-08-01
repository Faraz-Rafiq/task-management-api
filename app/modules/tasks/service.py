from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.tasks.repository import task_repository
from app.modules.tasks.schema import TaskCreate, TaskUpdate

class TaskService:

    def create_task(self, db: Session, task_data: TaskCreate, owner_id: int):
        return task_repository.create(db, task_data, owner_id)

    def get_task(self, db: Session, task_id: int, owner_id: int):
        task = task_repository.get_by_id(db, task_id, owner_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "error": {
                        "code": "TASK_NOT_FOUND",
                        "message": "Task not found"
                    }
                }
            )
        return task

    def get_all_tasks(self, db: Session, owner_id: int,
                      status: str = None, priority: str = None,
                      skip: int = 0, limit: int = 20):
        tasks, total = task_repository.get_all(
            db, owner_id, status, priority, skip, limit
        )
        return {"tasks": tasks, "total": total}

    def update_task(self, db: Session, task_id: int,
                    update_data: TaskUpdate, owner_id: int):
        task = self.get_task(db, task_id, owner_id)
        return task_repository.update(db, task, update_data)

    def delete_task(self, db: Session, task_id: int, owner_id: int):
        task = self.get_task(db, task_id, owner_id)
        task_repository.delete(db, task)
        return {"message": "Task deleted successfully"}

task_service = TaskService()