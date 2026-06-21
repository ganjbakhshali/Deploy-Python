# Todo API (FastAPI + SQLite)

A simple RESTful Todo API built with **FastAPI** and **SQLite**.  
This project demonstrates how to implement a basic CRUD API with proper request validation using **Pydantic**, structured routes, and persistent storage.

The API allows users to create, read, update, and delete tasks.

---

## Features

- RESTful API design
- FastAPI automatic documentation
- SQLite database storage
- Input validation using Pydantic
- Task status control using Enum
- Standard datetime format for task scheduling

---

## Project Structure

```
project/
│
├── main.py        # FastAPI application and API routes
├── database.py    # Database connection and CRUD operations
└── todo.db        # SQLite database (auto-created)
```

---

## Installation

1. Clone the repository:


2. Install dependencies:

    ```
    pip install fastapi uvicorn
    ```

---

## Running the API

Start the development server:

```
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | `/` | API health check |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a specific task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

# Testing the API with Postman

To test the API using **Postman**, follow these steps.

## 1. Create a Task

Request:

```
POST http://127.0.0.1:8000/tasks
```

In Postman:

1. Go to **Body**
2. Select **raw**
3. Select **JSON**
4. Send the following data:

```json
{
  "title": "deepLearning",
  "description": "study neural networks",
  "time": "2026-06-22 12:00:00",
  "status": "pending"
}
```

Response example:

```json
{
  "message": "Task created successfully"
}
```

---

## 2. Get All Tasks

Request:

```
GET http://127.0.0.1:8000/tasks
```

Example response:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "deepLearning",
      "description": "study neural networks",
      "time": "2026-06-22 12:00:00",
      "status": "pending"
    }
  ]
}
```

---

## 3. Get One Task

Request:

```
GET http://127.0.0.1:8000/tasks/1
```

---

## 4. Update a Task

Request:

```
PUT http://127.0.0.1:8000/tasks/1
```

Body (JSON):

```json
{
  "title": "deepLearning",
  "description": "study CNN architectures",
  "time": "2026-06-23 10:00:00",
  "status": "done"
}
```

---

## 5. Delete a Task

Request:

```
DELETE http://127.0.0.1:8000/tasks/1
```

Response:

```json
{
  "message": "Task deleted"
}
```

---

## Task Status Values

The API only accepts the following values for `status`:

```
pending
done
```

---

## Datetime Format

The `time` field must be sent in this format:

```
YYYY-MM-DD HH:MM:SS
```

Example:

```
2026-06-22 12:00:00
```

---

## Notes

- The SQLite database file (`todo.db`) is created automatically.
- FastAPI validates request data using Pydantic models.
- If invalid data is sent, the API returns a **422 validation error**.

---

## Educational Purpose

This project was created as a learning exercise to understand:

- FastAPI fundamentals
- REST API design
- SQLite integration
- Request validation with Pydantic
- CRUD operations in backend development
