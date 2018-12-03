'''
1) Write a program to apply various thresholding operations on the image
gradient.jpg. Apply the same with other similar images and analyze the
results.
THRESH_BINARY
THRESH_BINARY_INV
THESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.jpg',0)
#img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


plt.subplot(2,2,1);plt.imshow(img,'gray');plt.title("Oroginal Image"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,2);plt.imshow(th1,'gray');plt.title("THRESH_BINARY"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,3);plt.imshow(th2,'gray');plt.title("THRESH_BINARY_INV"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,4);plt.imshow(th4,'gray');plt.title("Trunc"); plt.xticks([]);plt.yticks([])
#plt.subplot(2,2,5);plt.imshow(th5,'gray');plt.title("ZERO"); plt.xticks([]);plt.yticks([])

plt.show()
