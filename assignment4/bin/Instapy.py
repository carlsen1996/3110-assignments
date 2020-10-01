import argparse
from instapy import grayscale_image as ipg
from instapy import sepia_image as ips
import cv2

"""This module will take in user agruments to make different changes to a picture"""


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
parser.add_argument('-se', '--sepia', action="store_true", default=False)
parser.add_argument('-g', '--gray', action="store_true", default=False)
parser.add_argument('-sc', '--scale')
parser.add_argument('-i', '--implement', default="numpy")
parser.add_argument('-o', '--out')

args = parser.parse_args()


if args.file == None:
    parser.print_help()
    exit(0)
    
img = cv2.imread(args.file)

if args.scale != None:
    width = img.shape[1] * int(args.scale)
    height = img.shape[0] * int(args.scale)
    dim = (width, height)
    img = cv2.resize(img, dim)

if args.sepia == False and args.gray == False:
    parser.print_help()
    exit(0)

if args.implement == "numpy" or args.implement == "python" or args.implement == "numba":
    if args.out != None:
        if args.sepia == True:
            ips.sepia_image(args.implement, img, args.out)
        if args.gray == True:
            ipg.grayscale_image(args.implement, img, args.out)
    else:
        if args.sepia == True:
            ips.sepia_image(args.implement, img)
        if args.gray == True:
            ipg.grayscale_image(args.implement, img)





