import numpy as np
import pandas as pd

class Day27:
    def __init__(self):
        print("kha is here")
        self.drink = pd.read_csv("drinks.csv")

    def testFunc(self):
        dataMap = dict();
        listMap = []
        groupData = self.drink.groupby('continent')
        #data2 = self.drink.agg('mean')['beer_servings']
        #print(groupData)
        for name,group in groupData:
            #print name
            dataMap = {'name':name,'val' : group['beer_servings'].mean()}
            listMap.append(dataMap)
        print listMap
        maxPricedItem = max(listMap, key=lambda x:x['val'])
        print("=============Max Bear value=========")
        print("Max Bear:",maxPricedItem)
        
    def getStatictic(self):
        dataMap = dict();
        listMap = []
        groupData = self.drink.groupby('continent')
        #print(groupData)
        for name,group in groupData:
            dataMap = {'name':name,
                       'bear_mean' : group['wine_servings'].mean(),
                       'count' : len(group['wine_servings']),
                       'std' : group['beer_servings'].std()
                       }
            listMap.append(dataMap)
        print("==============Statistic===============")
        print listMap

    def everyColumnMean(self):
        dataMap = dict();
        listMap = []
        groupData = self.drink.groupby('continent')
        #print(groupData)
        for name,group in groupData:
           
            dataMap = {'name':name,
                       'bear_mean' : group['beer_servings'].mean(),
                       'spirit_mean' : group['spirit_servings'].mean(),
                       'serving_mean' : group['wine_servings'].mean()
                       }
            listMap.append(dataMap)
        print("==============Mean for every content===============")
        print listMap

    def everyColumnMedian(self):
        dataMap = dict();
        listMap = []
        groupData = self.drink.groupby('continent')
        #print(groupData)
        for name,group in groupData:
           
            dataMap = {'name':name,
                       'bear_mean' : group['beer_servings'].median(),
                       'spirit_mean' : group['spirit_servings'].median(),
                       'serving_mean' : group['wine_servings'].median()
                       }
            listMap.append(dataMap)
        print("==============Median for every content===============")
        print listMap

    def meanMaxMin(self):
        dataMap = dict();
        print("==============Mean Max Min of spirit serviing===============")
        listMap = []
        print(self.drink['spirit_servings'].max())
        dataMap = {'mean':self.drink['spirit_servings'].mean(),
                   'max':self.drink['spirit_servings'].max(),
                   'min':self.drink['spirit_servings'].min(),

                   }
            
        
        print dataMap

        

s1 = Day27()
#s1.testFunc()
#s1.getStatictic()
#s1.everyColumnMean()
#s1.everyColumnMedian()
s1.meanMaxMin()



