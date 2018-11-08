import abc
class Vehicles:
    __metaclass__ = abc.ABCMeta
    def __init__(self,name,vehno,noWheel,presentVal):
        self.name = name
        self.vehno = vehno
        self.noWheel = noWheel
        self.presentVal = presentVal

    def show(self):
        print "name:%s,vehcle Number:%s,Number of wheel:%d,presentVal :%f"%(self.name,self.vehno,self.noWheel,self.presentVal)
    @abc.abstractmethod
    def calculate(self):
        pass
class Car(Vehicles):
    decAmount = 5000
    def calculate(self,year):
        self.presentVal =  self.presentVal -year * Car.decAmount
class Bus(Vehicles):
    decAmount = 1000
    def calculate(self,year):
        self.presentVal =  self.presentVal -year * Bus.decAmount
class Truck(Vehicles):
    decAmount = 12000
    def calculate(self,year):
        self.presentVal =  self.presentVal -year * Truck.decAmount
        
s1 = Car('Khan','Dl101',4,20000)
s1.calculate(2)
s1.show()
