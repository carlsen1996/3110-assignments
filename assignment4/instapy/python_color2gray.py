import cv2
import time


def python_color2gray(img):
    """this function uses only native python to change a picture from normal colors to gray
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
            if avg > 255:
                avg = 255
            z[0] = avg
            z[1] = avg
            z[2] = avg

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
        python_color2gray(img)
        cv2.imwrite("./output/pyrain_grey.jpg", img)
        toc = time.perf_counter()
        dur = toc - tic
        avg += dur

    avg = avg / 3

    f = open("./output/python_report_color2gray.txt", "w")
    f.write(
        f"Timing: python_color2gray\nAverage runtime running python_color2gray after 3 runs: {avg}\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
    f.close()
