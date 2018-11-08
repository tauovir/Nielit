class Employee:
    name=''
    empno=''
    basicpay = ''
    def __init__(self,pname,pempno,basicPay):
        self.name = pname
        self.empno = pempno
        self.basicPay = basicPay

    def display(self):
        print "name = %s,empno = %s,baiscpay = %s"%(self.name,self.empno,self.basicPay)

class Scientist(Employee):
    def __init__(self,name,empno,basicPay,pallowance,pcategory):
        Employee.__init__(self,name,empno,basicPay)
        self.allowance = pallowance
        self.category = pcategory
        
    def str1(self,s1):
        print s1.allowance
        print "Scientist : %s,with Id = %s,has salary of =%s"%(s1.name,s1.empno,(s1.basicPay + s1.allowance))

class Officer(Employee):
    def __init__(self,name,empno,basicPay,pGrade,dpt):
        Employee.__init__(self,name,empno,basicPay)
        self.grade = pGrade
        self.department = dpt
        
    def show(self,obj):
        print "Officer : %s,with Id = %s,has salary of =%s"%(obj.name,obj.empno,(obj.basicPay))
       



name1 = input("Enter Scientist name :")
epfno = input("Enter Scientist Id :")
basicpay1 = input("Enter basic pay :")
allowance1 = input("Enter allowance :")
category1 = input("Enter category :")
      
s1 = Scientist(name1,epfno,basicpay1,allowance1,category1)
s1.str1(s1)

name2 = input("Enter Officer name :")
epfn2 = input("Enter Officer Id :")
grade = input("Enter grade :")
dpt = input("Enter depatment :")
o1 = Officer(name2,epfn2,basicpay1,grade,dpt)
o1.show(o1)
