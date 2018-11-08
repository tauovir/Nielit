class Person:
    #define constructor
    def __init__(self,personName, personAge):
        self.name = personName
        self.age = personAge
    def showName(self):
        print self.name
        
    def showAge(self):
        print self.age
#Defining another class
class Student:
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId

#Multiple Inheritance

class Resident(Person, Student):
    def __init__(self, name, age, studentId):
        Person.__init__(self,name, age)
        Student.__init__(self, studentId)

resi1 = Resident('Khan',30 ,'Ai120')
resi1.showName()
resi1.showAge()
print resi1.getId()


        
    
    
        
        
