import matplotlib.pyplot as plt
import numpy as np


class MatPlot:
    def __init__(self):
        print("I ma calledd")
        
    def createMatPlot1(self):
        fobj = plt.figure(figsize = (6,6), facecolor = (1,0,1))
        fobj.canvas.set_window_title('Mat Plot Libraray')
        spobj1=fobj.add_subplot(221)
        spobj2=fobj.add_subplot(222,polar=True)
        spobj2=fobj.add_subplot(223)
        plt.show()

    def createLine(self):
        fobj=plt.figure(figsize=(4,4),facecolor=(1,0,0))
        spobj=fobj.add_subplot(1,1,1)
        an=np.random.randint(1,100,10)
        #yn=np.random.randint(1,100,10)
        #xn=np.arange(2,21,2)
        #yn.sort()
        #spobj.plot(xn,yn,linestyle='dashed',marker='d',markerfacecolor='r')
        yn=np.random.randint(1,100,10)
        xn=np.arange(2,21,2)
        yn.sort()
        print type(spobj)
        spobj.plot(xn,yn,'ro:',drawstyle='steps-mid')
        print 'xn=',xn
        print 'yn=',yn

        
        plt.show()

    def qa(self):
        fobj=plt.figure(figsize=(4,4),facecolor=(1,0,0))
        spobj=fobj.add_subplot(2,2,3)
        ranNum = np.random.randint(1,100,10)
        sortedNum = ranNum.sort()
        print(ranNum)
        print(sortedNum)
        y1 = ranNum[ranNum < 50]
        y2 = ranNum[ranNum > 50]
        print("==========")
        print y1
        print y2
        y2 = np.insert(y2,0,y1[-1])
        print("==========Resultant============")
        print(y2)
        evenNumber = np.arange(2,22,2)
        print("event number")
        print(evenNumber)
        #spobj.plot([x1, x2], [y1, y2], 'r')

    def qa1(self):
        fobj=plt.figure(figsize=(8,8))
        spobj=fobj.add_subplot(1,1,1)
        y = np.random.randint(1,100,10)
        y.sort()
        x=np.linspace(0,25,6)
        z = zip(x,y)
        print z
        for xi,yi in z:
            if yi < 50:
                spobj.plot(xi,yi,'ro:')
            else :
                spobj.plot(xi,yi,'go:')
                
        plt.show()

s1 = MatPlot()
#s1.createMatPlot1()
#s1.createLine()
s1.qa1()

