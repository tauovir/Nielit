import pandas as pd
import numpy as np
from pandas import DataFrame as frm
from pandas import Series as sr
#:1
data = np.arange(1,17).reshape(4,4)
#print(data)
#2
#MAsked array
data1 = np.ma.masked_array(data,mask = data%3 == 0)
#print(data1)
#3
dataFrame1 = frm(data1)
#print(dataFrame1)
#4
s1 = sr([1,2,3,4,5])
#print(s1)
s1.index = ['a','b','c','d','e']
#print(s1)
s1.index = ['e','d','a','b','c']
#print(s1)
s1 = s1.reindex(['e','d','a','b','c','f',])
#print(s1)
s1 = s1.reindex(['e','d','a','b','c','f'],method = 'bfill')

#========================Data Frame============================
a2 = np.arange(1,17).reshape(4,4)
#print(a2)
fa2 = frm(a2, index = 'a b c d'.split(), columns = 'c1,c2,c3,c4'.split(','))
fa2 = (fa2.reindex(index = list('abcde')))
fa2 = fa2.reindex(columns = "c1 c2 c3 c4 c5".split())
fa2 =fa2.fillna(0)
#print(fa2)
#**************************************************************
#6
arr = np.arange(1,17).reshape(4,4)
#7
fa22 = frm(arr, index = 'r1 r2 r3 r4'.split(), columns = 'c1,c2,c3,c4'.split(','))
#print(fa22)
x1 =(fa22.iloc[0,0]) #Scalar
x2 = sr((fa22.iloc[0,0])) # As Series
x3 = frm([x1]) # As Data frame
#print(x3)
#==Using BAse indexing
x1 = fa22.loc['r1']['c1']
#print(x1)
x2 = sr(fa22.loc['r1']['c1']) # As Series
x3 = frm([x1]) # As Data frame
#print(x2)
#=========last two row and two colums
#print(fa22.loc[['r3','r4'],['c3','c4']])

#=======================================
#8
arr1 = np.arange(1,17).reshape(4,4)
print("================")
#print(arr1)
frm2 = frm(arr1, index = "r3 r4 r5 r6".split(), columns = "c1 c2 c5 c6".split())
print(frm2)
print(fa22)
xx  = fa22.add(frm2,fill_value = 0).fillna(0)
print(xx)
xx1 = fa22.reindex(fa22.index.union(frm2.index),fill_value = 0) + frm2.reindex(fa22.index.union(frm2.index), fill_value = 0)
print(xx1.fillna(0))
