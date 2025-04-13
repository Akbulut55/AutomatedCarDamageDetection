from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("runs/detect/11n/weights/best.pt")
    metrics = model.val()
