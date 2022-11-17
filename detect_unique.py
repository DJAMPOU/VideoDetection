import cv2 as cv
import numpy as np

def unique_color(img, color):
    if color!="nothing":
        dim = np.shape(img)
        l_b = {}
        l_b["red"] = np.array([123, 121, 92])
        l_b["blue"] = np.array([100, 0, 0])
        l_b["green"] = np.array([40, 0, 0])
        l_b["white"] = np.array([0, 0, 0])
        l_b["black"] = np.array([0, 0, 0])

        h_b = {}
        h_b["red"] = np.array([360, 255, 255])
        h_b["blue"] = np.array([155, 255, 220])
        h_b["green"] = np.array([100, 255, 155])
        h_b["white"] = np.array([35, 45, 255])
        h_b["black"] = np.array([100, 255, 45])
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        try:
            mask = cv.inRange(hsv, l_b[color], h_b[color])
            img = cv.bitwise_and(img, img, mask=mask)
            img = cv.erode(img, (5, 5), iterations=3)
            img = cv.dilate(img, (5, 5), iterations=4)
        except:
            return img
    return img

def unique_form(img, form):
    print("nothing")
