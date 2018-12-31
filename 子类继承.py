# -*- coding:utf-8 -*-

class Dog(object):
    counter=0
    def __init__(self,name):
        self.name=name
        Dog.counter+=1
    def greet(self):
        print("hi,i am %s,my number is %d"%(self.name,Dog.counter))

class BarkingDog(Dog):
    def greet(self):
        print("woof ,i am %s,my nu is %d"%(self.name,Dog.counter))

if __name__=='__main__':
    dog=BarkingDog("Zoe")
    dog.greet()
    A=Dog("gre")
    A.greet()
