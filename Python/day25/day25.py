import pandas as pd
import numpy as np
from pandas import DataFrame as frm
import re

class Day25:
    def __init__(self):
        print("dddd")
        self.data = pd.read_csv('emp.csv',names = ['name','id','desig','salary','phone'])

    def answer(self):
        self.data2 = self.data
        self.data2['phone'] = self.data['phone'].apply(self.convert)
        print( self.data2)
    def convert(self,n):
        return re.sub('[^0-9]','', str(n))

s1 = Day25()
s1.answer()
