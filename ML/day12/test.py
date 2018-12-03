
import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture('car1.avi')
ret, frame = cap.read()
print frame
print cap.isOpened()
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





