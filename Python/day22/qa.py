import pandas as pd
import numpy as np
from pandas import Series as sr
from pandas import DataFrame as frm

dict1 = {
     'name':['taukir','khan','mango','rahul'],
     'country' :['India','canada','U.S','Europ'],
     'salary' : [251000,256000,14055,18900]
         }
df = frm(dict1)
df['dep'] = ['Developer','engineer','Designer','BDm']
#print df

#>>>>>>>>>>>>>>>>>>>Qa 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
s1 = sr('aa bb cc dd ee'.split())
df2 = frm(s1)
#print df2
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
s2 = sr('aa bb cc dd ee'.split())
s2.name = 'Series'
df3 = frm(s2)
#print df3
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
nparr = np.zeros((5,5))
#print nparr
print "==============================="
npDataFrame = frm(nparr)
#print npDataFrame
npDataFrame.columns = ["First", "Second","Third","Fourth","Fifth"]
#print "==============================="
#print npDataFrame
npDataFrame.index = list('abcde')
#print "==============================="
#print npDataFrame

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
nestDict = {'empId':{
            '1':'1001',
            '2' : '1002',
            '3' : '1003',
            '4' : '1004'
            },
            'name' :{
                '1' : 'Khan',
                '2' : 'Taukir',
                '3' : 'Pathan',
                '4' : 'Mango'
                },
            'salary' :{
                '1' : 25001,
                '2' : 12500,
                '3' : 16000,
                '4' : 25000
                }
            }

#print nestDict

df4 = frm(nestDict)
#print df4


#======================
s3 = sr('Engineer Developer designer codder'.split())
s3.name = 'Designation'
df4 = frm(s3)
#print df4

#===============
ss1 = sr(range(1,7))
ss2 = sr(range(11,67,11))
ss1.index = list('abcdef')
ss2.index = list('defxyz')

#xx= ss1.reindex(list('defxyz'))
s22 = ss1.append(ss2)
s22i = list('defxyz')
s22i.intersection(s22i)































































































































































































































































