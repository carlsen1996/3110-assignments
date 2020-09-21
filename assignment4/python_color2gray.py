import cv2
import time

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

    img = img.astype("uint8")
    cv2.imwrite("pyrain_grey.jpg", img)
    

img = cv2.imread('/home/carls/Documents/IN3110-johancb/assignment4/rain.jpg')    

avg = 0
for i in range(3):
    tic = time.perf_counter()
    python_color2gray(img)
    toc = time.perf_counter()
    dur = toc - tic
    avg += dur

avg = avg / 3

f = open("python_report_color2gray.txt", "w")
f.write(f"Timing: python_color2gray\nAverage runtime running python_color2gray after 3 runs: {avg}\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
f.close()
