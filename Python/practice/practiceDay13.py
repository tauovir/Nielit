import numpy as np
import pandas as pd
import xml.dom.minidom as dm

def createXmlFile():
    dataset = pd.read_csv('emp.csv',delimiter = ",")
    print(dataset.head())
    #Make Dom Object:
    doc = dm.Document()
    rootElement = doc.createElement('employees')
    data =dataset.iloc[:,0:4].values
    print("=============================")
    for item in data:
        #Make Id Element
        empElement = doc.createElement('employee')
        idElement = doc.createElement('id')
        idTextNode = doc.createTextNode(str(item[0]))
        idElement.appendChild(idTextNode)
        #Make Name Element
        nameElement = doc.createElement('name')
        nameTextNode = doc.createTextNode(item[1])
        nameElement.appendChild(nameTextNode)
        #Make Designation Element
        designationElement = doc.createElement('designation')
        desigTextNode = doc.createTextNode(item[2])
        designationElement.appendChild(desigTextNode)
        #Make Salary Element
        salaryElement = doc.createElement('salary')
        salaryTextNode = doc.createTextNode(str(item[3]))
        salaryElement.appendChild(salaryTextNode)
        #Append One by one each created element to employee element
        empElement.appendChild(idElement)
        empElement.appendChild(nameElement)
        empElement.appendChild(designationElement)
        empElement.appendChild(salaryElement)
        rootElement.appendChild(empElement)
    # Append final data to doc element
    doc.appendChild(rootElement)
    fd = open("createXml",'w')
    doc.writexml(fd, newl='\n')
    fd.close()
#createXmlFile()
#=====================Question 2==================
import MySQLdb as db
class MysqlDb:
    def __init__(self):
        self.con = db.connect("127.0.0.1",'root','','ai')
        self.cur = self.con.cursor()

s1 = MysqlDb()