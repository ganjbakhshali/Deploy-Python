# Todo API with FastAPI and Docker
A simple Todo API built with FastAPI, containerized with Docker.

# Project Structure
```
.
├── app
│   ├── database.py
│   └── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```
# Requirements
* Docker installed and running
# Build Docker Image
```
docker build -t todo-fastapi-app .
```
# Run Container
```bash
docker run -d -p 8000:80 --name todo-container todo-fastapi-app
```
# Access the App
* API root: http://localhost:8000
* Swagger docs: http://localhost:8000/docs

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