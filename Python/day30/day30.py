import scipy.optimize as spo
import scipy as sp
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame as f
from matplotlib import animation as anm
class Day30:
    def __ini__(self):
        print("Welcome to Scipy")

    def createGraph(self):
      x = [2,3,5,7,9]
      y = [4,5,7,10,15]
      xArr = np.array(x)
      yArr = np.array(y)
      fxf = lambda m,x,c:m*x + c
      popt, pcou = spo.curve_fit(fxf,x,y)
      #print(popt)
      vfxf = sp.vectorize(fxf)
      cy = vfxf(popt[0],x, popt[1])
      plt.plot(x,y,'r:*',label = "Observed")
      plt.plot(x,cy,'g-v',label = "Calculated")
      plt.legend(loc = 'best')
      plt.show()

    def animatedBarChar(self):
        fo=plt.figure(figsize=(6,6))
        so=fo.add_subplot(111)
        x=np.arange(5)
        xlabels='apple orange mango grapes banana'.split()
        sa=np.random.randint(1,90,5)
        bc1=so.bar(x,sa,align='center')
        so.set_xticks(x)
        so.set_xticklabels(xlabels)
    def animbar(i):
        global bc1
         sa=np.random.randint(1,90,5)
         print sa
         for bar1,h1 in zip(bc1,sa):
          bar1.set_height(h1)
         return bc1
        anm1=anm.FuncAnimation(fo,animbar,interval=3000)
        plt.show()
        
           
           
       
        

       
        
      


s1 = Day30()
#s1.createGraph()clear
s1.animatedBarChar()
