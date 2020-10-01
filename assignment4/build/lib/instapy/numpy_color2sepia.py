import numpy as np
import cv2
import time

def numpy_color2sepia(img):
    sepia_array = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
    img = img.dot(sepia_array.T)
    img[img > 255] = 255
    img = img.astype("uint8")
    return img
    

def test_time():
    img = cv2.imread("./rain.jpg")


        

    avg = 0
    for i in range(3):
        tic = time.perf_counter()
        sepia = numpy_color2sepia(img)
        cv2.imwrite("./output/nprain_sepia.jpg", sepia)
        toc = time.perf_counter()
        dur = toc - tic
        avg += dur


    avg = avg / 3
    pf = open("./output/python_report_color2sepia.txt", "r")
    line = pf.readline()
    line = pf.readline()
    pytime = float(line[-18:-2])
    fas =  pytime / avg


    f = open("./output/numpy_report_color2sepia.txt", "w")
    f.write(f"Timing: numpy_color2sepia\nAverage runtime running numpy_color2sepia after 3 runs: {avg}\nAverage runtime running of numpy_color2sepia is {fas} times faster than python_color2sepia\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
    f.close()