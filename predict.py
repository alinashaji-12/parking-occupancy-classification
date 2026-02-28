from ultralytics import YOLO
import cv2
import os

# 1. Print current working directory
print(f"Current Working Directory: {os.getcwd()}")

# Get absolute path of current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full model path safely
model_path = os.path.join(BASE_DIR, "model", "best.pt")

# 2. Print full model path and verify existence
print(f"Full Model Path: {model_path}")
print(f"Model file exists: {os.path.exists(model_path)}")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

# Load model
model = YOLO(model_path)

# Load image
image_path = os.path.join(BASE_DIR, "test_images", "sample.jpg")
print(f"Image Path: {image_path}")
print(f"Image file exists: {os.path.exists(image_path)}")

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found at: {image_path}")

# Run prediction
results = model(image_path)

probs = results[0].probs
if probs is not None:
    print("Prediction probabilities:", probs)
    print("Predicted class:", results[0].names[probs.top1])
else:
    print("No classification probabilities found, assuming detection task.")
    boxes = results[0].boxes
    if boxes is not None:
        print("Detected boxes:", boxes)