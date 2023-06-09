from yoloImageDetection import detectYoloModel
import multiprocessing


def sense(a):
    a.detect_wires("test_image.jpg")

def main():
    a = detectYoloModel()

    if(True):
        print("hello")
        p = multiprocessing.Process(target=sense,args=[a])
        p.start()

if __name__ == '__main__':
    main()