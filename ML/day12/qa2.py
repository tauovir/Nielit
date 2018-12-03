'''
Blend the images OpenCVLogo.png and ml.png using addWeighted function
in a 0.7:0.3 ratio. Try the same with other images.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('opencv-logo.png')
img2 = cv2.imread('ml.png')
img3 = cv2.imread('face.jpg')

blendedImage=cv2.addWeighted(img3,0.7,img2,0.3,0)

print img1.shape
print img2.shape
print img3.shape
cv2.imshow("Logo",img1)
cv2.imshow("Ml",img2)
cv2.imshow("Image 3",img3)
cv2.imshow("Blended Image",blendedImage)
cv2.waitKey(0)
