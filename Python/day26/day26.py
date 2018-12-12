import MySQLdb as db
import pandas as pd
import numpy as np
from sqlalchemy import create_engine as ce
import math
class Day26:
    def __init__(self):
        print("helloe")
        self.con = db.connect("127.0.0.1",'ai','ai','ai')
        self.result = [];
    def dataFrame1(self):
        data1 = pd.read_sql("select * from ai_20_emp",self.con)
        data2 = pd.read_sql("select * from ai_20_dpt",self.con)
        self.result = pd.merge(data1, data2, left_on = 'dptcode',right_on = 'dept_no',how = 'left')[['empno','name','dpt_nam','salary']].sort_values(by='salary', ascending=True)
        print(self.result)
    def storeDataToDB(self):
        if(len(self.result) > 0):
          cel = ce('mysql://ai:ai@127.0.0.1/ai')
          self.result.to_sql("ai_20_result",cel)
          print("Table Created")
    def readCsv(self):
        item = pd.read_csv('items.csv')
        sales = pd.read_csv('sales.csv')
        item = item.fillna(item['stock'].mean())    #Putt Nan to its mean value
        self.result = pd.merge(item, sales, left_on = 'id',right_on = 'tid')[['name','region','sale_qty']]
        print(self.result)
    def createPivot(self):
        if(len(self.result) > 0):
            self.result = self.result.pivot(columns = 'name', index = 'region')
            print("========Pivot====================")
            print(self.result)
        else:
            print("Record not found")
            
        


s1 = Day26()
#s1.dataFrame1()
#s1.storeDataToDB()
s1.readCsv()
s1.createPivot()

