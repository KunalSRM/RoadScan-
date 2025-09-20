import os
import yaml
from pathlib import Path

# Path for YOLO dataset
YOLO_DIR = "../data/yolo"

# Create YOLOv5 data YAML
data_yaml = {
    'train': os.path.join(YOLO_DIR, "images"),
    'val': os.path.join(YOLO_DIR, "images"),
    'nc': 1,
    'names': ["pothole"]
}

with open(os.path.join(YOLO_DIR, "pothole_data.yaml"), "w") as f:
    yaml.dump(data_yaml, f)

# Train YOLOv5
os.system(f"python yolov5/train.py --img 640 --batch 16 --epochs 50 "
          f"--data {os.path.join(YOLO_DIR, 'pothole_data.yaml')} "
          f"--weights yolov5s.pt --project ../models --name roadscan")
