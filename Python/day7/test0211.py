class Demo:
    def store(self):
        self.name = input("enter name:")
        self.salary= input("enter salary:")
    def display(self):
         print "name:",self.name
         print "salary:",self.salary
    
s1 = Demo()
s1.store()
s1.display()
