from . import numpy_color2sepia as nps
from . import numba_color2sepia as nbs
from . import python_color2sepia as pys
import cv2


def sepia_image(implement, img, output_filename=None):
    
    if implement == "numpy":
        sepia = nps.numpy_color2sepia(img)
    elif implement == "python":
        sepia = pys.python_color2sepia(img)
    elif implement == "numba":
        sepia = nbs.numba_color2sepia(img)
        
    sepia = nps.numpy_color2sepia(img)
    if output_filename != None:
        cv2.imwrite(output_filename, sepia)
    else:
        cv2.imwrite("output_sepia.jpg", sepia)
    return sepia