from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os

from model import predict_plate

app = FastAPI(title="Iranian License Plate Recognition API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "Plate Recognition API is running"}


@app.post("/predict-plate")
async def predict_plate_api(file: UploadFile = File(...)):

    if not file.content_type.startswith("image"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = predict_plate(file_path)
    except Exception:
        raise HTTPException(status_code=500, detail="Model processing failed")

    if result is None:
        raise HTTPException(status_code=404, detail="No license plate detected")

    return {
        "filename": file.filename,
        "plate_text": result
    }
