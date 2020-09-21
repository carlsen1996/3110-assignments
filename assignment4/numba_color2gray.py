from numba import jit

import cv2
import time

@jit(nopython=True)
def python_color2gray(img):
    for y in img:
        for z in y:
            red = z[0] * 0.21
            green = z[1] * 0.72
            blue = z[2] * 0.07
            avg = red + green + blue
            z[0] = avg
            z[1] = avg
            z[2] = avg


    

img = cv2.imread('/home/carls/Documents/IN3110-johancb/assignment4/rain.jpg')    

avg = 0
for i in range(3):
    tic = time.perf_counter()
    python_color2gray(img)
    toc = time.perf_counter()
    dur = toc - tic
    avg += dur

img = img.astype("uint8")
cv2.imwrite("numrain_grey.jpg", img)
avg = avg / 3

pf = open("python_report_color2gray.txt", "r")
line = pf.readline()
line = pf.readline()
time = float(line[-19:-1])
pyfas = time / avg
pf.close()

pf = open("numpy_report_color2gray.txt", "r")
line = pf.readline()
line = pf.readline()
time = float(line[-20:-1])
npfas = time / avg
pf.close()

f = open("numba_report_color2gray.txt", "w")
f.write(f"Timing: numba_color2gray\nAverage runtime running numba_color2gray after 3 runs: {avg}\nAverage runtime running of numba_color2gray is {pyfas} times faster than python_color2gray\nAverage runtime running of numba_color2gray is {npfas} times slower than numpy_color2gray\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
f.close()

