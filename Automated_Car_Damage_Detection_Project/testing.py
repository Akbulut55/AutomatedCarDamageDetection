from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
import cv2

# Load the trained model
model = YOLO('runs/detect/5n/weights/best.pt')

# Define the source of test images
source = 'car_damage_dataset_yolov5/test/images'
files = os.listdir(source)
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')
image_files = [file for file in files if file.endswith(image_extensions)]
num_images = len(image_files)

# Run inference on the test images
results = model.predict(source=source, save=True, conf=0.20)  # lower the confidence threshold to detect more(+mistakes)

# Display results
# output_dir = 'runs/detect/predict'
# predicted_images = os.listdir(output_dir)
#
# print("Test Results Saved in:", output_dir)
#
# # Display predictions
# for img_file in predicted_images[:10]:
#     img_path = os.path.join(output_dir, img_file)
#     image = cv2.imread(img_path)
#     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     plt.axis('off')
#     plt.show()
