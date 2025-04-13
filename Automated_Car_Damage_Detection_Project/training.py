from ultralytics import YOLO

if __name__ == "__main__":
    n_model = YOLO('yolov5n.pt')
    n_results = n_model.train(data="car_damage_dataset_yolov5/data.yaml", epochs=300, name='5n')
