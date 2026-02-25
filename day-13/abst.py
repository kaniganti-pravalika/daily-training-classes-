from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car starts with key")
c=car()
c.start()

#poly
class cal:
    def add(self,a,b=0,c=0):
        return a+b+c
calu=cal()
print(calu.add(5))
print(calu.add(5,10))
print(calu.add(5,10,15))

#method overriding
class Animal:
    def sound(self):
        print("Animals makes sound")
class dog(Animal):
    def sound(self):
        print("dog barks")
animal=Animal()
animal.sound()
Dog=dog()
Dog.sound()

#operator overloading
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
p1=point(2,3)
p2=point(4,5)
p3=p1+p2
print(p3.x,p3.y)

#magic methods
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    def __mul__(self,other):
        return self.pages*other.pages
b1=book(10)
b2=book(20)
print(b1+b2)
print(b1*b2)

#duck typing
class bird:
    def fly(self):
        print("birds can fly")
class airplane:
    def fly(self):
        print("airplane can fly")
def make_it_fly(obj):
    obj.fly()
Bird=bird()
plane=airplane()
make_it_fly(Bird)
make_it_fly(plane)