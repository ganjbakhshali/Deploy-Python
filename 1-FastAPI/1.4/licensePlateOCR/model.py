from ultralytics import YOLO
from hezar.models import Model
import cv2
import os

# -----------------------------
# Load models once
# -----------------------------
yolo_model = YOLO("best_plateDetection.pt")
ocr_model = Model.load("hezarai/crnn-fa-license-plate-recognition-v2")


def predict_plate(image_path: str):

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Invalid image")

    results = yolo_model.predict(img, conf=0.25, verbose=False)[0]

    crops = []

    for (x1, y1, x2, y2) in results.boxes.xyxy.cpu().numpy().astype(int):
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(img.shape[1], x2), min(img.shape[0], y2)

        crop = img[y1:y2, x1:x2].copy()
        crops.append(crop)

    if len(crops) == 0:
        return None

    plate_crop_path = "./images/plate_crop.jpg"
    cv2.imwrite(plate_crop_path, crops[0])

    plate_text = ocr_model.predict(plate_crop_path)

    return plate_text
