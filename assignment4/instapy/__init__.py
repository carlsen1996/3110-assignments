import numpy_color2gray
import numpy_color2sepia
import cv2


def grayscale_image(input_filename, output_filename=None):
    img = cv2.imread(input_filename)
    grey = numpy_color2gray(img)
    if output_filename != None:
        cv2.imwrite(output_filename, grey)
    else:
        cv2.imwrite("output_grey.jpg", grey)
    return grey

def sepia_image(input_filename, output_filename=None):
    img = cv2.imread(input_filename)
    sepia = numpy_color2sepia(img)
    if output_filename != None:
        cv2.imwrite(output_filename, sepia)
    else:
        cv2.imwrite("output_sepia.jpg", sepia)
    return sepia