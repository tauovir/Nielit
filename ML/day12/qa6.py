'''
Write a program to do face detection and eyes detection using
haarclassifiers.
'''

import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('cars.xml')
print car_cascade
img = cv2.imread('car.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1)
print cars
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
