from numba import jit

import cv2
import time

@jit(nopython=True)
def numba_color2sepia(img):
    for y in img:
        for z in y:
            red = z[0] * 0.393 + z[1] * 0.769 + z[2] * 0.189
            green = z[0] * 0.349 + z[1] * 0.686 + z[2] * 0.131
            blue = z[0] * 0.272 + z[1] * 0.524 + z[2] * 0.131
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            
            z[0] = blue
            z[1] = green
            z[2] = red
    return img


    

   
def test_time():
    avg = 0
    for i in range(3):
        img = cv2.imread('./rain.jpg') 
        tic = time.perf_counter()
        python_color2sepia(img)
        toc = time.perf_counter()
        dur = toc - tic
        avg += dur

    img = img.astype("uint8")
    cv2.imwrite("./output/numrain_sepia.jpg", img)
    avg = avg / 3

    pf = open("./output/python_report_color2sepia.txt", "r")
    line = pf.readline()
    line = pf.readline()
    time = float(line[-18:-1])
    pyfas = time / avg
    pf.close()

    pf = open("./output/numpy_report_color2sepia.txt", "r")
    line = pf.readline()
    line = pf.readline()
    time = float(line[-20:-1])
    npfas = time / avg
    pf.close()

    f = open("./output/numba_report_color2sepia.txt", "w")
    f.write(f"Timing: numba_color2sepia\nAverage runtime running numba_color2sepia after 3 runs: {avg}\nAverage runtime running of numba_color2sepia is {pyfas} times faster than python_color2sepia\nAverage runtime running of numba_color2sepia is {npfas} times slower than numpy_color2sepia\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
    f.close()
