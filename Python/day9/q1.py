class Vect:
    def __init__(self, px, py):
        self.x = px
        self.y = py
    def show(self):
        print "(%.2f,%.2f)"%(self.x,self.y)
    def __add__(self,obj):
       newx = self.x + obj.x
       newy = self.y + obj.y
       newV = Vect(newx, newy)
       return newV
       
    

obj1 = Vect(3.20,5.6)
obj2 = Vect(3.20,5.6)
obj1.show()
obj2.show()
obj3 = obj1 + obj2

obj3.show()

