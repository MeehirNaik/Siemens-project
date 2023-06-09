from yoloImageDetection import detectYoloModel

import time
# import multiprocessing
import threading
from queue import Queue

import cv2
import numpy as np
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution",
        default=[1280,720] ,
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args

def long_running_functions(frame,q):
    q.put(frame)
    print("Long run function")
    a = detectYoloModel()
    frame = a.detect_wires(frame)
    cv2.imshow("yolov8", frame)
    a = q.get()


def main():

    args = parse_arguments()
    frame_width, frame_hight = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_hight)
    q = Queue()
    
    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if (q.qsize() < 5):
            # Create a new process for each execution
            k = threading.Thread(target=long_running_functions,args=[frame,q])
            k.start()
        
        print(q.qsize())
        print("main is RUNNING")
        
        # Wait for 100ms
        time.sleep(1)
        
        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        
        if (cv2.waitKey(30) == 27):
            break
        
if __name__ == '__main__':
    main()