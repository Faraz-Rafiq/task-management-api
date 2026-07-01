from sqlalchemy.orm import Session
from app.modules.tasks.model import Task
from app.modules.tasks.schema import TaskCreate, TaskUpdate

class TaskRepository:

    def create(self, db: Session, task_data: TaskCreate) -> Task:
        task = Task(**task_data.model_dump())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def get_by_id(self, db: Session, task_id: int) -> Task | None:
        return db.query(Task).filter(Task.id == task_id).first()

    def get_all(self, db: Session, status: str = None, 
                priority: str = None, skip: int = 0, 
                limit: int = 20) -> tuple[list[Task], int]:
        query = db.query(Task)
        if status:
            query = query.filter(Task.status == status)
        if priority:
            query = query.filter(Task.priority == priority)
        total = query.count()
        tasks = query.offset(skip).limit(limit).all()
        return tasks, total

    def update(self, db: Session, task: Task, 
               update_data: TaskUpdate) -> Task:
        update_fields = update_data.model_dump(exclude_unset=True)
        for field, value in update_fields.items():
            setattr(task, field, value)
        db.commit()
        db.refresh(task)
        return task

    def delete(self, db: Session, task: Task) -> None:
        db.delete(task)
        db.commit()

task_repository = TaskRepository()