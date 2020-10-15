from numba import jit
import cv2
import time


@jit(nopython=True)
def numba_color2gray(img):
    """this function uses numba to change a picture from normal colors to grayscale
    Args: 
        img (array): This takes in a array of a picture
    returns:
        array: This returns a array of a picture where all the values is changed to be grayscale
    """
    for y in img:
        for z in y:
            red = z[0] * 0.21
            green = z[1] * 0.72
            blue = z[2] * 0.07
            avg = red + green + blue
            z[0] = avg
            z[1] = avg
            z[2] = avg
    return img


def test_time():
    """This tests the time of the function and creates a file of some descriptions. it also write the image to a 
    file in the output folder
    """
    img = cv2.imread('./rain.jpg')

    avg = 0
    for i in range(3):
        tic = time.perf_counter()
        numba_color2gray(img)
        toc = time.perf_counter()
        dur = toc - tic
        avg += dur

    img = img.astype("uint8")
    cv2.imwrite("./output/numrain_grey.jpg", img)
    avg = avg / 3

    pf = open("./output/python_report_color2gray.txt", "r")
    line = pf.readline()
    line = pf.readline()
    time = float(line[-19:-1])
    pyfas = time / avg
    pf.close()

    pf = open("./output/numpy_report_color2gray.txt", "r")
    line = pf.readline()
    line = pf.readline()
    time = float(line[-20:-1])
    npfas = time / avg
    pf.close()

    f = open("./output/numba_report_color2gray.txt", "w")
    f.write(
        f"Timing: numba_color2gray\nAverage runtime running numba_color2gray after 3 runs: {avg}\nAverage runtime running of numba_color2gray is {pyfas} times faster than python_color2gray\nAverage runtime running of numba_color2gray is {npfas} times slower than numpy_color2gray\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
    f.close()
