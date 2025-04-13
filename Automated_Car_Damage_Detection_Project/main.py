import csv
from ultralytics import YOLO
import os

# Initialize YOLO model
model = YOLO('runs/detect/11n/weights/best.pt')


# Load Image
def load_images_from_folder(folder_path):
    images = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            images.append(os.path.join(folder_path, file_name))
    return images


# Run Prediction on Single Image
def predict(image):
    results = model.predict(source=image, save=True, conf=0.20)
    boxes = results[0].boxes.data
    return len(boxes) if boxes is not None else 0


# Process All Images in the Folder
def process_images(images, output_csv):
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Image Name", "Label Count"])

        for image_path in images:
            image_name = os.path.basename(image_path)
            label_count = predict(image_path)
            writer.writerow([image_name, label_count])


# Prioritize Images by Label Count
def prioritize_images(csv_path, prioritized_csv):
    # Read CSV data
    data = []
    with open(csv_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row["Image Name"], int(row["Label Count"])))

    # Sort by label count in descending order
    data.sort(key=lambda x: x[1], reverse=True)

    # Write prioritized data to a new CSV
    with open(prioritized_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Image Name", "Label Count"])  # Header
        for image_name, label_count in data:
            writer.writerow([image_name, label_count])


# Main Process
def main(folder_path, output_csv, prioritized_csv):
    images = load_images_from_folder(folder_path)
    process_images(images, output_csv)
    prioritize_images(output_csv, prioritized_csv)
    print(f"Predictions saved to {output_csv} and prioritized list saved to {prioritized_csv}")


main("testimages", "predictions.csv", "prioritized_images.csv")
