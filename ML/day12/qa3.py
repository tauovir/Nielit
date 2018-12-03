'''
Apply adaptive thresholding to make the sudoku.jpg image more reader. Try
to do the same with other similar images.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('car.jpg',0)
blurImg = cv2.medianBlur(img,5)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


plt.subplot(2,2,1);plt.imshow(img,'gray');plt.title("Oroginal Image"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,2);plt.imshow(blurImg,'gray');plt.title("Blurr Image"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,3);plt.imshow(th2,'gray');plt.title("MEAN Adaptive Image"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,4);plt.imshow(th3,'gray');plt.title("Gausian Adaptive Image"); plt.xticks([]);plt.yticks([])

plt.show()
