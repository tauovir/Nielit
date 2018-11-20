import pandas as pd
import xml.dom.minidom as dm

data = pd.read_csv("emp.csv")
#print data
doc = dm.Document()
rootElement = doc.createElement('employees')
#print((data['ename']))
data = data.as_matrix()    # Make as two diamention array
for item in data:
    empElement = doc.createElement('employee')
    #Make <id>101</id>
    idElement = doc.createElement('id')
    idText = doc.createTextNode(str(item[0]))
    idElement.appendChild(idText)
    #Make <name>Anil</name>
    nameElement = doc.createElement('name')
    nameText = doc.createTextNode(item[1])
    nameElement.appendChild(nameText)
    #Make <designation>scientist</designation>
    designationElement = doc.createElement('designation')
    designationText = doc.createTextNode(item[2])
    designationElement.appendChild(designationText)
    #<salary>50000</salary>
    salaryElement = doc.createElement('salary')
    salaryText = doc.createTextNode(str(item[3]))
    salaryElement.appendChild(salaryText)
    #Append All Element
    empElement.appendChild(idElement)
    empElement.appendChild(nameElement)
    empElement.appendChild(designationElement)
    empElement.appendChild(salaryElement)
    rootElement.appendChild(empElement)
#Append all element to doc element
doc.appendChild(rootElement)
fd = open('f2.xml','w')
doc.writexml(fd, newl='\n')
fd.close()


