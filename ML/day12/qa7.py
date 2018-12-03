import cv2 as cv
import numpy as np
img=cv.imread('face.jpg',0)
edges=cv.Canny(img,50,200)
edges2=cv.Canny(img,0,120)
img1=np.hstack((img,edges,edges2))
cv.imshow('dst',img1)
cv.waitKey(0)
