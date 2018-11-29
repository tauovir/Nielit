import numpy as np
class Emp:
    def __init__(self):
        print "initialised"
        np.set_printoptions(precision=3)
        self.dataType = np.dtype({
            'names':['name','emp_id','designation','salary','phone'],
            'formats':['S20', 'i8', 'S20', 'f8', 'S20']
            })
        self.empData = np.loadtxt('emp.csv',delimiter=',',skiprows = 1, dtype = self.dataType)
        print self.empData
    def addRecord(self):
        print self.empData
        name = input("Enter employee name:")
        empId = input("Enter employee Id:")
        desig = input("enter employee Designation:")
        salary = input('Enter employee salary:')
        phon = input("Enter employee pnone no:")
        tpl = name,empId,desig,salary,phon
        newData = np.array([tpl], dtype = self.dataType)
        self.empData = np.concatenate([self.empData,newData])

    def displayDetail (self):
        name = input("Enter employee Name:")
        record = self.empData[self.empData['name'] == name]
        print record
        
    def displaySummary (self):
        salary = self.empData['salary'].sum()
        totalEmp = self.empData['salary'].size
        print "Total employee:",totalEmp,"Total Salary:",salary
        
    def saveAll (self):
        a = np.rec.array(self.empData)
        print a
        np.savetxt("foo.csv", a, delimiter=",")
    def removeEmp (self):
        print "Before Removing Employee:"
        print self.empData
        empno = input("Enter employee  Number")
        self.empData = self.empData[self.empData['emp_id'] != empno]
        print "After removing employee"
        print self.empData
        
s1 = Emp()
while(True):
    print "=================================="
    print "1 : Load Data"
    print "2 Add New Record"
    print "3  Delete Record"
    print "4  Display Detail"
    print "5  Display Summary"
    print "6  Save All"
    print "7  Exit"
    key1 = input("Enter Your Choise:")
   
    if (key1) == 1:#a
        s1 = Emp()
    elif (key1) == 2:#b
        s1.addRecord()
    elif (key1) == 3:#c
        s1.removeEmp()
    elif (key1) == 4:#d
        s1.displayDetail()
    elif (key1) == 5:
        s1.displaySummary()
    elif (key1) == 6:
        s1.saveAll()
    elif (key1) == 7:
        print "Bye Bye"
        break;
    else:
        print "enter above charecter"
    
    
    
#s1.addRecord()
#s1.displayDetail()
#s1.displaySummary()
#s1.saveAll()
#s1.removeEmp()

