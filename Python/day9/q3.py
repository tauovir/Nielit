class VectMul:
    def __init__(self, px, py):
        self.x = px
        self.y = py
    def show(self):
        print "(%d+%di)"%(self.x,self.y)
    def __mul__(self,obj):
       newy = self.x*obj.y + self.y * obj.x 
       newx = self.x * obj.x - self.y * obj.y
       newV = VectMul(newx, newy)
       return newV
         

obj1 = VectMul(3,2)
obj2 = VectMul(1,7)
obj1.show()
obj2.show()
obj3 = obj1 * obj2

obj3.show()

