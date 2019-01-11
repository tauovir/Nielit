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
        

#s1 = Scientist('Taukir khan',10001,12000,500,'It')
#s1.display()
#s2 = Officer('Taukir khan',10001,12000,'A+','Commando')
#s2.display()

#====================Day9==============
class Vect:
    '''
    Day9:
    First Question
    '''
    def __init__(self,px, py):
        self.x = px
        self.y = py
    def display(self):
        print("(%2f,%2f"%(self.x,self.y))
    def __add__(self,obj):
        self.x = self.x + obj.x
        self.y = self.y + obj.y
        result = Vect(self.x, self.y)
        return result

# s1 = Vect(25,30)
# s2 = Vect(25,60)
# s3 = s1 + s2
# s3.display()

class Vect2:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def display(self):
        #(a+bi) + (c+di) = (a+c) + (b+d)i
        print("(%d + %di) + (%d + %di) = (%d + %d) + (%d + %d)i"%(self.a,self.b,self.c,self.d,self.a,self.c,self.b,self.d))
    def __add__(self,obj):
        a1 =  self.a + obj.c
        b1 = self.b + obj.d
        c1 = self.a + obj.c
        d1 = self.b + obj.d
        
        result = Vect2(a1,b1,c1,d1)
        return result
    def showResult(self):
        #(a+bi) + (c+di) = (a+c) + (b+d)i
        print ("(%0.2f + %0.2fi) =  %0.2f + (%0.2f)i"%(self.a, self.b,self.c,self.d))


# s1 = Vect2(10,20,30,40)
# s1.display()
# #s2.display()
# print("************Result***********")
# s3 = s1 + s1
# s3.showResult()
#=======================DAy10===========================
def showAllException(cn, noh=0):
    print ('-'*noh ,cn.__name__)
    for scn in cn.__subclasses__():
        showAllException(scn,noh+2)
showAllException(Exception)



