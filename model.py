from pathlib import Path
import torch

def load_model(weights_path="yolov5s.pt"):
    """
    Load pretrained YOLOv5 model
    """
    model = torch.hub.load("ultralytics/yolov5", "custom", path=weights_path, force_reload=True)
    return model
