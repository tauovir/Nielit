import cv2 as cv
import numpy as np
img= np.zeros((512,512,3),np.int8)

#cv.line(img, (0,0),(400,400),(255,255,255),10)
cv.rectangle(img,(10,1),(500,100),(255,0,0),3)

cv.imshow("image",img)
cv.waitKey(0)
