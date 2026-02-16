''''print((lambda a,b:a+b)(5,3))
#higher order function
def square(num):
    return num**2
mynums=[1,2,3,4,5]
for x in mynums:
    print(square(x))

def square(num):
    return num**2
mynums=[1,2,3,4,5]
print(list(map(square,mynums)))

def inspect(name):
    i=len(name)
    if i%2==0:
        return "even"
    else:
        return name[0]
print(list(map(inspect,["pravali","sai","kavya"])))

#filtering the elements using filter function
def even(num):
    return num%2==0
mynums=[1,2,3,4,5,6,7,8,9]
print(list(filter(even,mynums)))'''
#reduce function
from functools import reduce
def multiply(x,y):
    return x*y
mynums=[1,2,3,4]
product=reduce(multiply,mynums)
print(product)

