import cv2 as cv
import numpy as np
#Read image
img = cv.imread('apple.jpg',0)

rows,cols = img.shape
m = np.float32([
    [1,0,100],
    [0,1,150]
    ])
dst = cv.warpAffine(img, m,(cols, rows))
cv.imshow("Apple",dst)
cv.imshow("Apple2",img)
# Hold image till anyt key pressed
cv.waitKey(0)
