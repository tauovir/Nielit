import cv2 as cv
import numpy as np

class Day13:
    def __init__(self):
        #self.img = cv.imread("man.jpg")
        #self.img = cv.imread("girl.jpg")
        self.img = cv.imread("car.jpg")
        self.kernel = np.ones((2,2),np.uint8)
        #cv.imshow("Image",self.img)
    def showErrosion(self):
        erossion = cv.erode(self.img , self.kernel, iterations = 1)
        cv.imshow("Errosion",erossion)
    def showDilate(self):
        erossion = cv.dilate(self.img , self.kernel, iterations = 1)
        cv.imshow("Dialate",erossion)
    def morphology1(self):
         #erossion = cv.morphologyEx(self.img ,cv.MORPH_CLOSE, self.kernel)
         erossion = cv.morphologyEx(self.img ,cv.MORPH_OPEN, self.kernel)
         cv.imshow("Morpho logy",erossion)
    def removeNoise(self):
         #erossion = cv.morphologyEx(self.img ,cv.MORPH_CLOSE, self.kernel)
         erossion = cv.morphologyEx(self.img ,cv.MORPH_OPEN, self.kernel)
         cv.imshow("Morpho logy",erossion)
    def sobelExm(self):
        sobelx=cv.Sobel(self.img,cv.CV_64F,1,0,ksize=1)
        sobely=cv.Sobel(self.img,cv.CV_64F,0,1,ksize=1)
        cv.imshow('Sobel',sobely)


s1 = Day13()
#s1.showErrosion()
#s1.showDilate()
#s1.morphology1()
#s1.removeNoise()
s1.sobelExm()

cv.waitKey(0) 
