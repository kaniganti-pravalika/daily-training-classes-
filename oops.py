'''class A:
    print('Sanam Teri Kasam')
class A:
    pass
obj=A()
print(obj)
class A:
    def func(self):
        print('chaava')
obj=A()
obj.func()

#operations
class A:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
    def modu(self,a,b):
        print(a%b)
obj=A()
obj.add(10,5)
obj.sub(10,5)
obj.mul(10,5)
obj.div(34,2)
obj.modu(30,5)

class A:
    def add(self,a,b):
        print(a+b)
class B:
    def sub(self,a,b):
        print(a-b)
class C:
    def mul(self,a,b):
        print(a*b)
class D:
    def div(self,a,b):
        print(a/b)
class E:
    def modu(self,a,b):
        print(a%b)
obj=A()
obj.add(30,50)
obj=B()
obj.sub(45,20)
obj=C()
obj.mul(44,2)
obj=D()
obj.div(33,3)
obj=E()
obj.modu(5,2)

class A:
    def __init__(self):
        print("Fifty Grades of Gray")
obj=A()

class A:
    def __init__(self):
        print(id(self))
obj=A()
print(id(obj))

class A:
    def __init__(self):
        print("constructor")
obj=A()
obj1=A()
obj2=A()
obj3=A()

class city:
    def hyd(self):
        print("Charmina")
    def __init__(self,hyd):
        print("hyd")
    def vizag(self):
        print("vizag beach")
    def __init__(self,viz):
        print("vizag")
obj=city()
obj.hyd()
obj.vizag()

class A:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

obj = A("vivake", 1017, 8.5)

print(obj.name)
print(obj.roll)
print(obj.marks)

class A:
    def __init__(self):
        print("VJIT",id(self))
obj=A()
obj.__init__()

class A:
    def __init__(self):
        print("VJIT")
    def __init__(self,X):
        print("Vaagdevi",X)
obj=A(10)

class info:
    def __init__(self,name,rollno,address,college,branch):
        self.name=name
        self.rollno=rollno
        self.address=address
        self.college=college
        self.branch=branch
        print(id(self))
    def details(self):
        print(self.name,self.rollno,self.address,self.college,self.branch)
        print(id(self))
obj=info("pavalika",588,"khammam","VCE","CSE")
obj.details()

class movie:
    def __init__(self,name,hero,heroine,rating):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.rating=rating
    def info(self):
        print('movie name:',self.name)
        print('hero name:',self.hero)
        print('heroine name:',self.heroine)
        print('movie rating:',self.rating)
    movies=[movie('bahubali','prabhas','anushka'),]'''
