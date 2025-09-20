import os
import shutil
import xml.etree.ElementTree as ET

# Paths
DATA_DIR = "../data"
IMAGES_DIR = os.path.join(DATA_DIR, "images")
ANNOTATIONS_DIR = os.path.join(DATA_DIR, "annotations")
YOLO_DIR = os.path.join(DATA_DIR, "yolo")

os.makedirs(YOLO_DIR, exist_ok=True)
os.makedirs(os.path.join(YOLO_DIR, "images"), exist_ok=True)
os.makedirs(os.path.join(YOLO_DIR, "labels"), exist_ok=True)

# Map classes
CLASSES = ["pothole"]

def convert_annotation(xml_file, label_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    w = int(root.find("size/width").text)
    h = int(root.find("size/height").text)
    lines = []
    for obj in root.iter("object"):
        cls_id = CLASSES.index(obj.find("name").text)
        xml_box = obj.find("bndbox")
        xmin = int(xml_box.find("xmin").text)
        ymin = int(xml_box.find("ymin").text)
        xmax = int(xml_box.find("xmax").text)
        ymax = int(xml_box.find("ymax").text)
        # Normalize for YOLO format
        x_center = ((xmin + xmax) / 2) / w
        y_center = ((ymin + ymax) / 2) / h
        width = (xmax - xmin) / w
        height = (ymax - ymin) / h
        lines.append(f"{cls_id} {x_center} {y_center} {width} {height}")
    with open(label_file, "w") as f:
        f.write("\n".join(lines))

# Convert all XML files
for xml_file in os.listdir(ANNOTATIONS_DIR):
    if xml_file.endswith(".xml"):
        img_name = xml_file.replace(".xml", ".jpg")
        shutil.copy(os.path.join(IMAGES_DIR, img_name),
                    os.path.join(YOLO_DIR, "images", img_name))
        label_file = os.path.join(YOLO_DIR, "labels", xml_file.replace(".xml", ".txt"))
        convert_annotation(os.path.join(ANNOTATIONS_DIR, xml_file), label_file)

print("✅ Dataset converted to YOLOv5 format.")
