import cv2
import torch
from ultralytics import YOLO
import supervision as sv
import os

class detectYoloModel:
    def __init__(self) -> None:
        self.model = YOLO("yolov8n.pt")
        self.box_annotator = sv.BoxAnnotator(
            thickness=2,
            text_thickness=2,
            text_scale=1
        )
        self.image_files = []
        self.label_name = []
        self.xywhn_data = []

    def convert_xywh_to_xywhn(self, xywh, image_width, image_height):
        tensor = xywh

        # Extract the values
        values = tensor[0].tolist()
        # print(values)

        # Round off values to six decimal places
        rounded_values = ["{:.6f}".format(val) for val in values]

        # print(rounded_values)
        return rounded_values

    def yolov8_auto_label_single_image(self,img_to_detect):
        img_to_detect = cv2.imread(img_to_detect)
        img_to_detect = cv2.resize(img_to_detect,(640,480))
        result = self.model(img_to_detect)[0]
        class_ids = result.boxes.cls.int().tolist()
        # print(class_ids,"class_ids") 
        self.label_name = []
        self.xywhn_data = []
        for res in result:
            boxes = res.boxes  # Boxes object for bbox outputs
            tensor = res.boxes.cls

            # Extract the values
            values = tensor[0].tolist()
            self.label_name.append(res.names.get(int(values)))
            self.xywhn_data.append(
                self.convert_xywh_to_xywhn(
                    boxes.xywhn, 
                    image_width= 640, 
                    image_height=480))
        print("**********************************************") 
        return self.label_name, self.xywhn_data

    def get_images_files_name(self,image_folder_path):
        self.image_folder_path = image_folder_path
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        self.image_files = []

        for root, dirs, files in os.walk(self.image_folder_path):
            for file in files:
                _, extension = os.path.splitext(file)
                if extension.lower() in image_extensions:
                    self.image_files.append(os.path.join(root, file))
        print(self.image_files)
        return self.image_files
        

a = detectYoloModel()
print(11/9)
frame = a.get_images_files_name(r"New folder")

for fra in frame:
    label, xywhn_data = a.yolov8_auto_label_single_image(fra)
    for la, fr in zip(label, xywhn_data):
        print(la,fr)

    # print(label, xywhn_data)