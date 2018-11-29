'''
Write a program apply scaling on the image of the apple with
scaling factor 2 on both x and y axes.
'''
import cv2 as cv
import numpy as np
#Read image
img = cv.imread('apple.jpg',0)

rows,cols = img.shape
dst = cv.resize(
    img,None,
    fx = 3,
    fy = 1,
    interpolation = cv.INTER_CUBIC
    )
cv.imshow("apple", dst)
cv.imshow("apple2", img)
# Hold image till anyt key pressed
cv.waitKey(0)
