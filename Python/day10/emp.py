import abc
class Employee:
    __metaclass__ = abc.ABCMeta
    def __init__(self,name,empno,basicPay):
        self.name = name
        self.empno = empno
        self.basicPay = basicPay
        self.hra = 0
        self.da = 0
        self.spa = 0
        self.salary = 0
         
    def show(self):
        print "name:%s,emp Id:%s,Salary Pay:%f,"%(self.name,self.empno,self.salary)
    @abc.abstractmethod
    def getDa(self):
        pass
    @abc.abstractmethod
    def getHra(self):
        pass
    @abc.abstractmethod
    def getSpa(self):
        pass
    def calSalary(self):
        self.salary = self.basicPay + self.hra + self.da + self.spa
        
#Derived Class
class Officer(Employee):
    def getDa(self):
        self.da =  self.basicPay * 30/100
    def getHra(self):
        self.hra =  self.basicPay * 10/100
    def getSpa(self):
        self.spa =  self.basicPay * 10/100
#===========derived Class=========
class Engineer(Employee):
    pass
class SEng(Engineer):
    def getDa(self):
        self.da =  self.basicPay * 30/100
    def getHra(self):
        self.hra =  self.basicPay * 10/100
    def getSpa(self):
        self.spa =  self.basicPay * 20/100 + 1000 
        
class JEng(Engineer):
    def getDa(self):
        self.da =  self.basicPay * 30/100
    def getHra(self):
        self.hra =  self.basicPay * 10/100
    def getSpa(self):
        self.spa =  self.basicPay * 20/100 + 500
#=====Officer object=====        
s1 = Officer('khan officer','Ai-120',5000)
s1.getDa()
s1.getHra()
s1.getSpa()
s1.calSalary()
s1.show()
#=====Senior Engineer=======
s2 = SEng('khan Sener enf','Ai-120',5000)
s2.getDa()
s2.getHra()
s2.getSpa()
s2.calSalary()
s2.show()
#=====Junior Engineer=======
s3 = JEng('khan Junior enf','Ai-120',5000)
s3.getDa()
s3.getHra()
s3.getSpa()
s3.calSalary()
s3.show()

