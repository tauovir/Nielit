class Demo:
    def __init__(self,pname,psalary):
        self.name = pname
        self.salary= psalary
    def display(self):
         print "name:",self.name
         print "salary:",self.salary
    
s1 = Demo("khan",55)
s1.display()
