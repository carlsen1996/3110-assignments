from . import numpy_color2gray as npg
from . import numba_color2gray as nbg
from . import python_color2gray as pyg
import cv2


def grayscale_image(implement, img, output_filename=None):
    """This function uses the different methods to change the picture in to a grayscale image
    args:
        implement (string): This is the type of method the user wants to use {numpy, python, numba}
        img (array): This is the array of the picture
        output_filename (string): (optional) This is the name of the output file
    returns:
        array: It returns an array of the changed picture
    """

    
    if implement == "numpy":
        gray = npg.numpy_color2gray(img)
    elif implement == "python":
        gray = pyg.python_color2gray(img)
    elif implement == "numba":
        gray = nbg.numba_color2gray(img)

    if output_filename != None:
        cv2.imwrite(output_filename, gray)
    else:
        cv2.imwrite("output_grey.jpg", gray)
    return gray