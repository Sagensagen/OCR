
import numpy as np
import cv2



def pre_process_characer(input_img):
    try:
        opencvImage = cv2.cvtColor(np.array(input_img), cv2.COLOR_RGB2BGR)
        ret, thresh = cv2.threshold(opencvImage,127,255,cv2.THRESH_BINARY_INV)
        gray_img = cv2.cvtColor(np.array(thresh), cv2.COLOR_RGB2GRAY)
        kernel = np.ones((1,1),np.uint8)
        # erode_img = cv2.erode(gray_img, kernel, iterations=1)
        # erode_img = rotate(erode_img)
        return gray_img
    except:
        print("fek")



def rotate(img):
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return img

