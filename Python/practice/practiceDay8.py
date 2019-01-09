class Empployee:
    name = ''
    empno = 0
    basicPay = 0
    def __init__(self,name, empno,basicPay):
        self.name = name
        self.empno = empno
        self.basicPay = basicPay
class Scientist(Empployee):
    def __init__(self,name, empno,basicPay,allowance,category):
        Empployee.__init__(self,name, empno,basicPay)
        self.allowance = allowance
        self.category = category
    def display(self):
        print("***********Display Scientist Data**********")
        print("Name:",self.name)
        print("EmpNo::",self.empno)
        print("Basic Pay:",self.basicPay)
        print("Allowance:",self.allowance)
        print("Category:",self.category)

class Officer(Empployee):
    def __init__(self,name, empno,basicPay,grade,department):
        Empployee.__init__(self,name, empno,basicPay)
        self.grade = grade
        self.department = department
    def display(self):
        print("***********Display Officer Data**********")
        print("Name:",self.name)
        print("EmpNo::",self.empno)
        print("Basic Pay:",self.basicPay)
        print("Grade:",self.grade)
        print("Department:",self.department)
        

s1 = Scientist('Taukir khan',10001,12000,500,'It')
s1.display()
s2 = Officer('Taukir khan',10001,12000,'A+','Commando')
s2.display()
