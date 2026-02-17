def compute(x,func):
    return func(x)
def double(n):
    return n*2
def square(n):
    return n**2
result=compute(3,double)+compute(2,square)
print(result)

def vjit(n):
    if n==0:
        return 1
    else:
        return n*vjit(n-1)
def vivek(a,b):
    return vjit(a)+vjit(b)
result=vivek(3,4)
print(result)

def a():
    return [1,2,3]
for i in a():
    print(i+1-i**i,end=' ')

