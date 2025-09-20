import torch
import cv2
from src.model import load_model

# Load trained model
model = load_model(weights_path="../models/roadscan/weights/best.pt")

def predict_image(img_path):
    results = model(img_path)
    results.print()  # Show predictions in console
    # Save results image with bounding boxes
    results.save(save_dir="predictions")
    return results
