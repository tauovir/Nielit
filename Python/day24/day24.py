import  pandas as pd
import numpy as np
from pandas import DataFrame as frm
print "khan"

arr = np.random.randint(10,20,40)
arr = arr.reshape(10,4)
dataFrame = frm(arr,columns = ['c1','c2','c3','4'])
#print dataFrame
dataFrame = dataFrame.sort_values('c1')
#print "Ascending Order"
#print dataFrame

dataFrame = dataFrame.sort_values('c3',ascending = True)
#print "=========Descending Order=========="
#print dataFrame
#========================Data Frame choise=====================

class Demo:
    def __init__(self):
        dataset = [['BMW','INDIA',5000],['AUDI','CANADA',7000],['MARUTI','U.S',80000],['SKODA','NEWZEALAND',9000]]
        a1 = np.array(dataset).reshape(4,3)
        self.dataFrame = frm(a1,columns = ['Item','Place','totalSale'])
        print self.dataFrame
    def addData(self):
        item  = input("Enter Item Name:")
        place = input("enter Country name:")
        sale = input('enter sale amount:')
        list1 = [item,place,sale]
        
        self.dataFrame.iloc[-1] = list1
        self.dataFrame.index = self.dataFrame.index + 1
        print self.dataFrame


s1 = Demo()
s1.addData()
