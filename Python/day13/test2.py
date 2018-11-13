import pandas as pd
import xml.dom.minidom as dm

data = pd.read_csv("emp.csv")
#print data
doc = dm.Document()
rootElement = doc.createElement('employees')

for df in data:
    print data[df][0]

""""
for roll,name in data['eno']:
    empElement = doc.createElement('employee')
    rollEle = doc.createElement('roll')
    rollText = doc.createTextNode(str(roll))
    rollEle.appendChild(rollText)
    empElement.appendChild(rollEle)
    rootElement.appendChild(empElement)
    """
    
name = doc.createElement('name')
"""
rollText = doc.createTextNode(name)
roll.appendChild(rollText)
    
nameText = doc.createTextNode()

designation = doc.createElement('designation')
designationText = doc.createTextNode()

salary = doc.createElement('salary')
salaryText = doc.createTextNode()
"""
#rootElement.appendChild(rollEle)
doc.appendChild(rootElement)
fd = open('f2.xml','w')
doc.writexml(fd)
fd.close()


