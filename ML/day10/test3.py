'''
. Write a program to rotate the apple image 45 degrees
'''
import cv2 as cv
import numpy as np
#Read image
img = cv.imread('apple.jpg',0)

rows,cols = img.shape
m = cv.getRotationMatrix2D(
    ((cols - 1)/2, (rows - 1)/2), 30,1)
dst = cv.warpAffine(img, m,(cols, rows))
cv.imshow("apple", dst)
cv.imshow("apple2", img)
# Hold image till anyt key pressed
cv.waitKey(0)
