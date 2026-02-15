n=int(input())
if n%2==0:
    print((n//2**3))
else:
    print(((n+1)//2)**2)
a,b,c=int(input()),int(input()),int(input())
max=a
if b>max:
    max=b
if c>max:
    max=c
print("lm=",max)
n=int(input())
if n%2==0:
    print((n//2**3))
else:
    print(((n+1)//2)**2)

w=0
for i in range(10):
    if(i%2!=0):
        w=w+50
    elif(i%2==0):
        w=w-10
    else:
        w=w-5
if w>500:
    w=w
    
a=int(input())
b=int(input())
c=int(input())
if(a>b):
    if(a>c):
        print("A is big")
    elif(a==c):
        print("A and C are equal")
    else:
        print("C is big")
elif(a==b):
    print("A and B are equal")
    
elif(b>c):
    print("B is big")
elif(b==c):
    print("B and C are equal")
else:
    print("all are equal")
