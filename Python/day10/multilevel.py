class Animal:
    def eat(self):
        print "eating"
        
#Defining another class
class Dog(Animal):
    def bark(self):
        print "Dos is barking"

#Multiple Inheritance

class BabyDog(Dog):
    def weep(self):
        print "Weeping..."

s1 = BabyDog()
s1.eat()
s1.bark()
s1.weep()



        
    
    
        
        
