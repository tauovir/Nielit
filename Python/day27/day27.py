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
        

s1 = Day27()
s1.testFunc()
