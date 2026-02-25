class demo:
    class_var="I am a Class Variable "
    def Show_Variable(self):
        Local_var="I am a Local Variable"
        self.instance_var="I am an instance variable"
        print(Local_var)
        print(self.instance_var)
        print(demo.class_var)
obj=demo()
obj.Show_Variable()

class car:
    wheel=4
    def __init__(self,name,color):
        self.name=name
        self.color=color
car1=car("BMW","Red")
car2=car("Audi","Black")
car3=car("Tesla","White")

print("Initially")
print(car1.name,car1.color,car1.wheel)
print(car2.name,car2.color,car2.wheel)
print(car3.name,car3.color,car3.wheel)


car.wheel=2
print("\n After changing class variable")
print(car1.name,car1.color,car1.wheel)
print(car2.name,car2.color,car2.wheel)
print(car3.name,car3.color,car3.wheel)

car2.color="blue"
print("\n After changing class variable")
print(car1.name,car1.color,car1.wheel)
print(car2.name,car2.color,car2.wheel)
print(car3.name,car3.color,car3.wheel)

class S:
    s_n="VJIT"
    @classmethod
    def change_school(cls,name):
        cls.s_n=name
S.change_school("CBIT")
print(S.s_n)

class s:
    @staticmethod
    def greet():
        print("Hello, Welcome to the OOP world")
s.greet()
