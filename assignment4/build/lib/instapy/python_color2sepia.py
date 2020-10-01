import cv2
import time

def python_color2sepia(img):
    for y in img:
        for z in y:
            red = z[0] * 0.393 + z[1] * 0.769 + z[2] * 0.189
            green = z[0] * 0.349 + z[1] * 0.686 + z[2] * 0.131
            blue = z[0] * 0.272 + z[1] * 0.524 + z[2] * 0.131
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            
            z[0] = blue
            z[1] = green
            z[2] = red
            

    img = img.astype("uint8")
    return img
    

    

def test_time():    

    avg = 0
    for i in range(3):
        img = cv2.imread('./rain.jpg')
        tic = time.perf_counter()
        python_color2sepia(img)
        cv2.imwrite("./output/pyrain_sepia.jpg", img)
        toc = time.perf_counter()
        dur = toc - tic
        avg += dur

    avg = avg / 3

    f = open("./output/python_report_color2sepia.txt", "w")
    f.write(f"Timing: python_color2sepia\nAverage runtime running python_color2sepia after 3 runs: {avg}\nTiming performed using: time.perf_counter()\nThe dimentions of the image is {img.shape}")
    f.close()