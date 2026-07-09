# FastAPI Docker App

  

A minimal **FastAPI** application containerized with **Docker**.

  

This project shows how to package a simple API, install dependencies from `requirements.txt`, and run it inside a container.

  

# Project Structure

```

project/

├── app/

│ └── main.py

├── Dockerfile

├── requirements.txt

└── readme.md
```
  

## Application Endpoints

### `GET /`

Returns a simple welcome response.

Example response:

```                                           

{  
  "Hello": "World"  
}  

```
### GET /items/{item_id}

Returns the `item_id` and an optional query parameter `q`.

Example request:

                                         

GET /items/5?q=test  

Example response:

                                          
```
{  
  "item\_id": 5,  
  "q": "test"  
}  
```
## Requirements

Make sure you have installed:

-   Docker
-   Python dependencies listed in `requirements.txt`

  

## Dockerfile Overview

This project follows this workflow:

-   Uses a Python base image
-   Sets `/code` as the working directory
-   Copies `requirements.txt`
-   Installs dependencies
-   Copies the application source code
-   Runs the FastAPI app on port `80`

## Build the Docker Image

Run this command in the project root directory:

                                         

docker build -t fastapi-docker-app .  

## Run the Container

                                         

docker run -d -p 80:80 --name fastapi-container fastapi-docker-app  

## Access the API

After running the container, open:

-   API root: `http://localhost`
-   Swagger UI: `http://localhost/docs`
-   ReDoc: `http://localhost/redoc`

## Stop and Remove the Container

Stop the container:

                                        

docker stop fastapi-container  

Remove the container:

                                        

docker rm fastapi-container  

## Notes

-   Application entry point: `app/main.py`
-   Container start command:

                                          

fastapi run app/main.py --port 80  

For local development with auto-reload:

                                          

uvicorn app.main:app --reload  

## Educational Purpose

This project is useful for learning:

-   FastAPI basics
-   Dockerizing a Python web application
-   Container image building
-   Port mapping
-   API documentation with Swagger UI and ReDoc