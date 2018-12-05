import cv2 as cv
import numpy as np
img= np.zeros((400,400,3),np.int8)
#print img
img[1:50,1:50] = (0,250,0)
cv.imshow("image",img)
cv.waitKey(0)
