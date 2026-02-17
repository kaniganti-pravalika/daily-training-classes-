#function  with no parameters and no return type
def greet():
    print("Morning")
greet()
def add(a,b):
    return a+b
result = add(12,66)
print("The sum is:", result)
#function with multiple return values
def Arithmetic(a,b):
    addition=a+b
    subtraction=a-b
    multiplication=a*b
    division=a/b
    moduler=a%b
    return addition,subtraction,multiplication,division,moduler
result=Arithmetic(12,5)
print("The addition is:",result[0])
print("The subtraction is:",result[1])  
print("The multiplication is:",result[2])
print("The division is:",result[3])
#function with default parameters
def P():
    print("P" ,end="")
def R():
    print("R",end="")
def A():
    print("A", end="")
def V():
    print("V" ,end="")
def A():
    print("A",end="")
def L():
    print("L",end="")
def I():
    print("I",end="")
def K():
    print("K",end="")
def A():
    print("A",end="")
P()
R()
A()
V()   
A()
L()
I()
K()
A()
#passing the parameters to the function
def greet(name,a):
    print("good mornig ",name,a+a)
    print("How are you?",name,a**a)
greet("pravali",4)
#return type of function
def greet(name):
    return 'good morning',name
print(greet('pravalika'))
hai=greet('pravalika')
print(hai)
#function calling another function
def hyd():
    print("the hyd is famous for biriyani")
def delhi():
    print("the delhi is famous for paratha")
def mumbai():
    print("the mumbai is famous for vada pav")
def chenni():
    print("the chenni is famous for idly")
def kolkata():
    print("the kolkata is famous for rasgulla")
    hyd()
hyd()
#recusssion
'''
def  clg_name():
    print("vaagdevi",end="")
    clg_name()
clg_name()'''
# positional arguments
def grocery(name,price):
    print("item name is",name,"its price is",price)
grocery(name="bread",price=20)
grocery(price=150,name="butter")
#default arguments
def greet(name,msg="good morning"):
    print("hello",name,msg)
greet("pravalika")
greet("pravalika","how are you?")

radius=int(input("enter the radius of the circle:"))

def cal_area(radius,pi=3.14):
    area=pi*radius**2
    return area
result=cal_area(radius)
print("the area of the circle is:",result)

#function with variable length arguments
def addnos(*a):
    return sum(a)
print(addnos(10,20))
print(addnos(10,20,30))
# variable length keyword arguments
def largest_string(*strings):
    if not strings:
        return "tuple is empty"
    
    largest = strings[0]
    
    for s in strings:
        if len(s) > len(largest):
            largest = s

    return largest, len(largest)
name, length = largest_string("cat", "elephant", "dog")

print("Largest string:", name)
print("Length:", length)


def findlargest(*name):
    max=0
    for s in  name:
        if len(s)>max:
            max=len(s)
    return max
print(findlargest("january","february","march"))

