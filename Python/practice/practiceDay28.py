import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def firstMatplot():
    framObj = plt.figure(figsize = (6,6), facecolor=(1,0,1))
    framObj.canvas.set_window_title("First Mat Plot Graph")
    subObj1 = framObj.add_subplot(221)
    subObj2 = framObj.add_subplot(222,polar = True)
    subObj3=framObj.add_subplot(223)
    
    plt.show()

#firstMatplot()

def createLine():
    frmObj = plt.figure(figsize=(6,6), facecolor=(1,0,1))
    frmObj.canvas.set_window_title("Create Line")
    subObj = frmObj.add_subplot(111)
    y = np.random.randint(1,100,10)
    x = np.arange(2,21,2)
    print(y)
    print(x)
    y.sort()
    subObj.plot(x,y, linestyle='dashed',marker='d',markerfacecolor='r')

    plt.show()

def qa():
        fobj=plt.figure(figsize=(8,8))
        spobj=fobj.add_subplot(1,1,1)
        y = np.random.randint(1,100,10)
        y.sort()
        x=np.linspace(0,25,10)
        z = zip(x,y)
        print(x)
        print(y)
        for xi,yi in z:
            if yi < 50:
                spobj.plot(xi,yi,'ro:')
            else :
                spobj.plot(xi,yi,'go:')
                
        plt.show()

# createLine()
qa()