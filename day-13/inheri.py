'''class Animal:
    def speak(self):
        print("Animal makes a Sound")
class dog(Animal):
    def bark(self):
        print("Dog Barks")
obj=dog()
obj.speak()#Animal makes a Sound
obj.bark()#Dog Barks'''
#with out constructro
class school:
    def display_info(self,name,age):
        print("name:",name,"age:",age)
class student(school):
    def display_student_info(self, grade):
        print("grade:",grade)
class teacher(school):
    def display_teacher_info(self, subject):
        print("subject:",subject)
obj=student()
obj.display_info("varun",23)
obj.display_student_info("A")
obj1=teacher()
obj1.display_info("madhu",35)
obj1.display_teacher_info("science")
#with constructor
class School:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name,"age:",self.age)
class Student(School):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        print("grade:",grade)
class Teacher(School):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
        print("subject:",subject)
obj=Student("anu",21,"A")
obj.display()

obj1=Teacher("madhu",32,"maths")
obj1.display()


class parent:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("name:",name,"roll:",roll)
    def addres(self, houseno):
        print("houseno:", houseno)


class child(parent):
    def __init__(self, name, roll, age):
        parent.__init__(self, name, roll)   # calling parent constructor
        self.age = age
        print("Age:", age)

    def girl(self, fav_color):
        print("favorate color", fav_color)


obj = child("ram", 2345, 19)
obj.girl("pink")
obj.addres("4-123")

class parent:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        print("name:",self.name,"\n","parent Roll:",self.roll)
    def addres(self,houseno):
        print("parent houseno:",houseno)
class child(parent):
    def __init__(self,name,roll):
        parent.__init__(self,name,roll)
        self.roll=roll
        print("child roll:",roll)
    def address(self,houseno):
        print("child house no:",houseno)
obj=child("rama",213)
obj.addres("5-123")
obj.addres("4-123")

#multiple inheritance
class A:
    def __init__(self,B,**kwargs):
        self.B=B
        super().__init__(**kwargs)
    def show(self):
        print("class A name:",self.B)
class C:
    def __init__(self,D,**kwargs):
        self.D=D
    def display(self):
        print("class C name:",self.D)
class E(A,C):
    def __init__(self,F,B,D,**kwargs):
        super().__init__(B=B,D=D)
        self.F=F
        print("class E name:",self.F)
obj=E(12,32,22)
obj.B
obj.D
obj.F
obj.show()
obj.display()
#multi level inheritance
class Suman():
    def __init__(self,name):
        self.name=name
        print("name:",name)
class Ramana(Suman):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("Age:",age)

class Uma(Ramana):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll
        print("roll:",roll)
obj=Uma("ram",23,526)
#hybrid inheritance
class Suman:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)
        print("Name:", self.name)

class Ramana(Suman):
    def __init__(self, age, **kwargs):
        self.age = age
        super().__init__(**kwargs)
        print("Age:", self.age)

class Uma(Suman):
    def __init__(self, roll, **kwargs):
        self.roll = roll
        super().__init__(**kwargs)
        print("Roll:", self.roll)

class Ram(Ramana, Uma):
    def __init__(self, name, age, roll, Class):
        self.Class = Class
        # Pass all parent args as keyword args
        super().__init__(age=age, roll=roll, name=name)
        print("Class:", self.Class)

# Create object
obj = Ram(name="Ajay", age=24, roll=456, Class="CSE")