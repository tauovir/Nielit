'''
Make the opencvlogo smoother by applying blur function. Try it with other
images
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencvlogo.png')
blurImg = cv2.blur(img,(20,15))

plt.subplot(2,2,1);plt.imshow(img,'gray');plt.title("Oroginal Image"); plt.xticks([]);plt.yticks([])
plt.subplot(2,2,2);plt.imshow(blurImg,'gray');plt.title("Blurr Image"); plt.xticks([]);plt.yticks([])

plt.show()
