from yoloImageDetection import detectYoloModel
# from PIL import Image
import cv2


cap = cv2.VideoCapture(0)
ret, frame = cap.read()

a = detectYoloModel()
results = a.detect_wires(frame)
print("frame",frame)
print("results",results)

output_path = r"Output_Results\output_bus.jpg"
cv2.imwrite(img=results,filename = 'local.jpg')