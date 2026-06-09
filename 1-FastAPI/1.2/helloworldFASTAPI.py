from fastapi import FastAPI

app = FastAPI()

@app.get("/ali")
async def root():
    return {"message": "Hello World"}