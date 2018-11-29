'''
Write a program to find out whether there is any difference
between two images
'''
import cv2 as cv
import numpy as np

#Read image
img1 = cv.imread('apple.jpg')
img2 = cv.imread('orange.jpg')
resul = img1 - img2
r1 = resul
data = r1[r1!=0]
print data.size 
if data.size > 1:
    print "Images are diffrence"
else:
   print "Images are same"
cv.imshow("apple2", resul)
# Hold image till anyt key pressed
cv.waitKey(0)

#orang RGB(255,165,0),BGR(0,165,255)
`
