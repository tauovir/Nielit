class DemoVector:
    def __init__(self, a, b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def show(self):
        #print "(%.2f,%.2f)"%(self.x,self.y)
        #(a+bi) + (c+di) = (a+c) + (b+d)i
        print "(%0.2f + %0.2fi) + (%0.2f + %0.2fi) =  (%0.2f + %0.2f) + (%0.2f + %0.2f)i"%(self.a, self.b,self.c,self.d,self.a, self.c, self.b, self.d)
    def showResult(self):
        #(a+bi) + (c+di) = (a+c) + (b+d)i
        print "(%0.2f + %0.2fi) =  %0.2f + (%0.2f)i"%(self.a, self.b,self.c,self.d)
    def __add__(self,obj):
       a1 = self.a + obj.c
       b1 = self.b + obj.d
       c1 = self.a + obj.c
       d1 = self.b + obj.d
       newV = DemoVector(a1, b1, c1, d1)
       return newV
       
    bj1 = DemoVector(3.2,5.3,10.20,6.3)
obj1.show()
obj3 = obj1 + obj1

obj3.showResult()



