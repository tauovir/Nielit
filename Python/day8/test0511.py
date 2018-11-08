class Employee:
    name=''
    empno=''
    basicpay = ''
    def __init__(self,pname,pempno,basicPay):
        self.name = pname
        self.empno = pempno
        self.basicPay = basicPay
        #print "basic pay=", self.basicPay

    def display(self):
        print "name = %s,empno = %s,baiscpay = %s"%(self.name,self.empno,self.basicPay)

class Scientist(Employee):
    def __init__(self,name,empno,basicPay,pallowance,pcategory):
        Employee.__init__(self,name,empno,basicPay)
        self.allowance = pallowance
        self.category = pcategory
        
    def show(self):
        print "name = %s,empno = %s,basic pay =%s"%(self.name,self.empno,self.basicPay)
        print "allowance = %s,category = %s"%(self.allowance,self.category)

class Officer(Employee):
    def __init__(self,name,empno,basicPay,pGrade,dpt):
        Employee.__init__(self,name,empno,basicPay)
        self.grade = pGrade
        self.department = dpt
        
    def show(self):
        print "name = %s,empno = %s,basic pay =%s"%(self.name,self.empno,self.basicPay)
        print "Grade = %s,department = %s"%(self.grade,self.department)


name1 = input("Enter name :")
epfno = input("Enter employe no :")
basicpay1 = input("Enter basic pay :")
allowance1 = input("Enter allowance :")
category1 = input("Enter category :")

grade = input("Enter grade :")
dpt = input("Enter depatment :")


       
s1 = Scientist(name1,epfno,basicpay1,allowance1,category1)
o1 = Officer(name1,epfno,basicpay1,grade,dpt)
s1.show()
o1.show()
