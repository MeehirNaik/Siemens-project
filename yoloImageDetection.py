import cv2

from ultralytics import YOLO
import supervision as sv

class detectYoloModel:
    def __init__(self) -> None:
        self.model = YOLO("best.pt")
        self.box_annotator = sv.BoxAnnotator(
            thickness=2,
            text_thickness=2,
            text_scale=1
        )

    def detect_wires(self,img_to_detect):
        # img_to_detect = cv2.imread(img_to_detect)
        img_to_detect = cv2.resize(img_to_detect,(640,480))
        result = self.model(img_to_detect)[0]

        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{self.model.model.names[class_id]} {confidence:0.2f}"
            for _, _, confidence, class_id, _ in detections
        ]

        frame = self.box_annotator.annotate(
            scene=img_to_detect,
            detections=detections,
            labels=labels
        )

        self.final_image = frame

        return frame
        # cv2.imshow("yolov8 live", frame)
        # while True:
        #     if (cv2.waitKey(30) == 27):
        #         break

# a = detectYoloModel()
# frame = a.detect_wires("test_image.jpg")
# cv2.imshow("yolov8 live", frame)
# while True:
#     if (cv2.waitKey(30) == 27):
#         break