'''
. Write a program to obtain the negative of a grayscale image
(hint:subtract 255 from all pixels values)
'''

import cv2 as cv
import numpy as np
#Read image
img1 = cv.imread('apple.jpg')


img1 = 255-img1
print img1

cv.imshow("apple2", img1)
# Hold image till anyt key pressed
cv.waitKey(0)

#orang RGB(255,165,0),BGR(0,165,255)
