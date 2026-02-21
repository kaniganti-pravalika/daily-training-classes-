
num=[1,2,3,25,5]
count=1
Max=num[0]
for i in range(1,len(num)):
        if Max<num[i]:
            count+=1
            Max=num[i]
print(count)

E=[7,0,5,1,3]
L=[1,2,1,3,4]
current=0
mx=0
for i in range(len(E)):
    current=E[i]-L[i]+current
    mx=max(mx,current)
print(mx)