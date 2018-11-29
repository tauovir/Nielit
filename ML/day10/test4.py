
import cv2 as cv
import numpy as np
#Read image
img1 = cv.imread('apple.jpg')
img2 = cv.imread('orange.jpg')
rows1,cols1 = img1.shape[:-1]
rows2,cols2 = img2.shape[:-1]

img1 = img1[0:rows1,0:cols1/2] # Half portion of apple
img2 = img2[0:rows2,cols2/2:cols2] # half portion of orange

vis = np.concatenate((img1, img2), axis=1)

cv.imshow("apple2", vis)
# Hold image till anyt key pressed
cv.waitKey(0)

#orang RGB(255,165,0),BGR(0,165,255)
