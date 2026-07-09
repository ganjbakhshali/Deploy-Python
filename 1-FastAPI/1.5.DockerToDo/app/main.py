from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
import database as database


app = FastAPI(title="Todo API")

class TaskStatus(str, Enum):
    pending = "pending"
    done = "done"

class TaskCreate(BaseModel):
    title: str
    description: str
    time: datetime
    status: TaskStatus

database.create_tables()

@app.get("/")
def root():
    return {"message": "Todo API is running"}

@app.get("/tasks")
def get_tasks():
    tasks = database.read_all_tasks()
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: TaskCreate):
    try:
        formatted_time = task.time.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format")

    database.add_task(
        task.title,
        task.description,
        formatted_time,
        task.status.value
    )

    return {"message": "Task created successfully"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    existing_task = database.read_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    database.update_task(
        task_id,
        task.title,
        task.description,
        task.time.strftime("%Y-%m-%d %H:%M:%S"),
        task.status.value
    )

    return {"message": "Task updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    existing_task = database.read_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    database.delete_task(task_id)

    return {"message": "Task deleted"}

@app.get("/tasks/{task_id}")
def get_one_task(task_id: int):
    task = database.read_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
