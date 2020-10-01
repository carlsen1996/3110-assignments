from instapy import grayscale_image as ipg
from instapy import sepia_image as ips
import cv2
import numpy as np
img = cv2.imread('./rain.jpg')

# def test_gray_with_output():
#     instapy.grayscale_image(img, "/home/carls/Documents/test_output_grey.jpg")

# def test_gray_without_output():
#     instapy.grayscale_image(img)

# def test_sepia_with_output():
#     instapy.sepia_image(img, "test_output_sepia.jpg")

# def test_sepia_without_output():
#     instapy.sepia_image(img)

def test_grey_shape():
    grey = ipg.grayscale_image("numpy", img)
    assert len(grey.shape) == 2

def test_sepia_shape():
    sepia = ips.sepia_image("numpy", img)
    assert len(sepia.shape) == 3

def test_gray_pixel():
    img = cv2.imread('./rain.jpg')
    gray = ipg.grayscale_image("numpy", img)
    img = np.dot(img[...,:3], [0.21, 0.72, 0.07])
    img = img.astype("uint8")
    assert img[113, 67] == gray[113, 67]

def test_sepia_pixel():
    img = cv2.imread('./rain.jpg')
    sepia = ips.sepia_image("numpy", img)
    sepia_array = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
    img = img.dot(sepia_array.T)
    img[img > 255] = 255
    img = img.astype("uint8")
    assert img[231, 46, 1] == sepia[231, 46, 1]

