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
'''class sch:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name,"age:",self.age)
class stu(sch):
    def __init__(self,grade):
        print("grade:",grade)
class tea(sch):
    def __init__(self,subject):
        print("subject:",subject)
obj=stu("anu",21;"A")
obj.display()
obj=tea("madhu",)'''

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


        
        