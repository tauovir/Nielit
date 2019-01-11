import re
import pandas as pd

def qa1():
    dataset = pd.read_csv("emp1.csv",delimiter=",")
    data = dataset.iloc[:,0:5].values
    
    fd = open("onlyScientist.csv","w")
    for row in data:
        pattern = r'scie'
        if re.match(pattern,row[2]):
            #st1 = ' '.join(row)
            str1 = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3])
            fd.write(str1)
            fd.write("\n")
    fd.close()

def qa2():
    dataset = pd.read_csv("emp1.csv",delimiter=",")
    data = dataset.iloc[:,0:5].values
    
    fd = open("ini.csv","w")
    for row in data:
        pattern = r'^[Mm]'
        if re.match(pattern,row[0]):
            #st1 = ' '.join(row)
            str1 = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3])
            fd.write(str1)
            fd.write("\n")
    fd.close()

def qa4():
    dataset = pd.read_csv("emp1.csv",delimiter=",")
    data = dataset.iloc[:,0:5].values
    
    fd = open("empphno.csv","w")
    for row in data:
        pattern = '\{\}|\(|\)|\[|\]|-|_'
       # pattern = '\{|\}|\(|\)\-|\[|\]|-|_'
        str1 = re.sub(pattern,'',row[4])
        text = row[0] +"," + str(str1)
        fd.write(text)
        fd.write("\n")
    fd.close()
    print("********Finished***********")
    
def qa5():
    dataset = pd.read_csv("emp1.csv",delimiter=",")
    data = dataset.iloc[:,0:5].values
    
    fd = open("emp200.csv","w")
    for row in data:
        pattern = r'\d{3}'
        searchData = re.search(pattern,str(row[1]))
        if searchData:
            val = int(searchData.group())
            if val > 200:
                str1 = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3])
                fd.write(str1)
                fd.write("\n")

    fd.close()
    print("********Finished***********")
            
#qa1()
#qa2()
#qa4()
qa5()
