import numpy as np
import cv2
import time


def numpy_color2gray(img):
    """this function uses numpy to change a picture from normal colors to gray
    Args: 
        img (array): This takes in a array of a picture
    returns:
        array: This returns a array of a picture where all the values is changed to be grayscale
    """
    img = np.dot(img[..., :3], [0.21, 0.72, 0.07])
    img[img > 255] = 255
    img = img.astype("uint8")
    return img


def test_time():
    """This tests the time of the function and creates a file of some descriptions. it also write the image to a 
    file in the output folder
    """
    img = cv2.imread('./rain.jpg')

    avg = 0
    for i in range(3):
        tic = time.perf_counter()
        grey = numpy_color2gray(img)
        cv2.imwrite("./output/nprain_grey.jpg", grey)
        toc = time.perf_counter()
        dur = toc - tic
        avg += dur

    avg = avg / 3
    pf = open("./output/python_report_color2gray.txt", "r")
    line = pf.readline()
    line = pf.readline()
    pytime = float(line[-19:-2])
    fas = pytime / avg

    f = open("./output/numpy_report_color2gray.txt", "w")
    f.write(
        f"Timing: numpy_color2gray\nAverage runtime running numpy_color2gray after 3 runs: {avg}\nAverage runtime running of numpy_color2gray is {fas} times faster than python_color2gray\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
    f.close()
