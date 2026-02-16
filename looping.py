a=int(input("enter the number :"))

for i in range(1,11):
    print(a,"*",i,"=",a*i)
a=int(input("enter the number :"))
i=0
while(i<=10):
    print(a,"*",i,"=",a*i)
    i=i+1
if 100:
    pass
print("no")
i=1
count=0
for i in range(50):
    if i%2==0:
        continue
    print(i,end=" ")
    count=count+1
print(count)
i=1
count=0
for i in range(50):
    if i%2==0 and i%3==0:
        print(i,end=" ")
        count=count+1
print(count)
i=8
for i in range(100):
    if i%8==0:
        print(i,end=" ")
        
i=8
count=0
for i in range(100):
    if i%8==0:
        print(i,end=" ")
        count=count+1
print(count)



a=int(input("enter the value :" ))
if(a==1):
    for i in range(100):
        print(i+1,end=" ")
elif(a==2):
    i=1
    while(i%2==0):
        if i<100:
            continue
    print(i,end=" ")
    i=i+1
elif(a==3):
    i=0
    while(i%2==0):
        if i==66:
            break
            print(i,end=" ")
    i=i+1
            
elif(a==4):
    i=1
    for i in range(50):
        if i%2==0 and i%3==0:
            if(i==12):
                continue
            print(i,end=" ")
else:
    print("invalid input")
  
        
