import instapy
import cv2
import numpy as np

# def test_gray_with_output():
#     instapy.grayscale_image('./rain.jpg', "/home/carls/Documents/test_output_grey.jpg")

# def test_gray_without_output():
#     instapy.grayscale_image('./rain.jpg')

# def test_sepia_with_output():
#     instapy.sepia_image('./rain.jpg', "test_output_sepia.jpg")

# def test_sepia_without_output():
#     instapy.sepia_image('./rain.jpg')

def test_grey_shape():
    grey = instapy.grayscale_image('./rain.jpg')
    assert len(grey.shape) == 2

def test_sepia_shape():
    sepia = instapy.sepia_image('./rain.jpg')
    assert len(sepia.shape) == 3

def test_gray_pixel():
    img = cv2.imread('./rain.jpg')
    gray = instapy.grayscale_image('./rain.jpg')
    img = np.dot(img[...,:3], [0.21, 0.72, 0.07])
    img = img.astype("uint8")
    assert img[113, 67] == gray[113, 67]

def test_sepia_pixel():
    img = cv2.imread('./rain.jpg')
    sepia = instapy.sepia_image('./rain.jpg')
    sepia_array = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
    img = img.dot(sepia_array.T)
    img[img > 255] = 255
    img = img.astype("uint8")
    assert img[231, 46, 1] == sepia[231, 46, 1]

