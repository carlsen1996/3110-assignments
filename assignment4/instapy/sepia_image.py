from . import numpy_color2sepia as nps
from . import numba_color2sepia as nbs
from . import python_color2sepia as pys
import cv2


def sepia_image(implement, img, output_filename=None):
    """This function uses the different methods to change the picture in to a sepia image
    args:
        implement (string): This is the type of method the user wants to use {numpy, python, numba}
        img (array): This is the array of the picture
        output_filename (string): (optional) This is the name of the output file
    returns:
        array: It returns an array of the changed picture
    """
    
    if implement == "numpy":
        sepia = nps.numpy_color2sepia(img)
    elif implement == "python":
        sepia = pys.python_color2sepia(img)
    elif implement == "numba":
        sepia = nbs.numba_color2sepia(img)
        
    sepia = nps.numpy_color2sepia(img)
    if output_filename is not None:
        cv2.imwrite(output_filename, sepia)
    else:
        cv2.imwrite("output_sepia.jpg", sepia)
    return sepia