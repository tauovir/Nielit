import pandas as pd
from pandas import Series as sr
print pd.__version__

l1 = [10,203,55,30,60]

s1 = sr(l1)
print s1
#===First two element
print s1[0]
print s1[1]

s1.index = list('abcde')
print s1

dict1 = dict(apple = 100, mango = 200, orange = 500, grapes = 600)

sr1 = sr(dict1)
print sr1
