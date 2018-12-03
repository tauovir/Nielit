import  pandas as pd
import numpy as np
from pandas import DataFrame as frm

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
#========================Data Frame choise Question=====================

class Demo:
    def __init__(self):
        dataset = [['BMW','INDIA',5000],
        ['AUDI','CANADA',7000],
        ['MARUTI','U.S',80000],
        ['SKODA','NEWZEALAND',9000]
        ]
        a1 = np.array(dataset).reshape(4,3)
        self.dataFrame = frm(a1,columns = ['Item','Place','totalSale'])
        print (len(self.dataFrame))
    # Description: Add New Data to Dataframe
    def addData(self):
        item  = input("Enter Item Name:")
        place = input("enter Country name:")
        sale = input('enter sale amount:')
        list1 = [item,place,sale]
        arr1 = np.array([list1])
        newDataFrame = frm(arr1,columns = ['Item','Place','totalSale'],index = [len(self.dataFrame)])
        self.dataFrame = self.dataFrame.append(newDataFrame)
        print (self.dataFrame)
    # Description: Get rank of given Item by place wise
    def placeWiseRank(self):
        ItemName  = input("enter Item name:")
        print(self.dataFrame.rank)
        self.dataFrame['pRank'] = self.dataFrame['Place'].rank()
        print("========Placewise rank=========")
        print(self.dataFrame)
        rank = 0
        for i in range(len(self.dataFrame)):
            if self.dataFrame['Item'][i] == ItemName:
                rank = self.dataFrame['pRank'][i]
                break
        print("Rank of Item:" + ItemName + ":"+str(rank))

   # Description: Get rank of given Item by Item wise
    def itemWiseRank(self):
        ItemName  = input("enter Item name:")
        print(self.dataFrame.rank)
        self.dataFrame['iRank'] = self.dataFrame['Item'].rank()
        print("========Item wise rank=========")
        print(self.dataFrame)
        for i in range(len(self.dataFrame)):
            if self.dataFrame['Item'][i] == ItemName:
                rank = self.dataFrame['iRank'][i]
                break
        print("Rank of Item:" + ItemName + ":"+str(rank))

s1 = Demo()
while(True):
    print ("==================================")
    print ("1 : Add Data")
    print ("2 : Place wise rank")
    print ("3 : Item wise rank")
    print ("7  Exit")
    key1 = input("Enter Your Choise:")
    key1 = int(key1)
    if key1 == 1:
        s1.addData()
    elif key1 == 2:
        s1.placeWiseRank()
    elif key1 == 3:
        s1.itemWiseRank()
    elif key1 == 7:
        print ("Bye Bye")
        break;
    else:
        print ("enter above charecter")
    
