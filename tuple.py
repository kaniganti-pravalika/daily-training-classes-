#swaping
a=[1,2,3,4,5,6]
a[0],a[-1]=a[-1],a[0]
print(a)
#rotation left&right
a=[1,2,3,4,5,6]
#left rotation
a=a[1:]+a[:1]
print(a)
#right rotation
a=[1,2,3,4,5,6]
a=a[-1:]+a[:-1]
print(a)
#addeding indexes to list
l=[1,2,3,4,5,6]
for i in range(len(l)):
    print(l[i]+1+i ,end="")
'''
#sum of max and min
l=[5,6,3,0,2,9,1,4]
min=l[0]
max=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
    elif l[i]<min:
        min=l[i]
print("The sum of max and min is:",max+min)'''
#output=0,0,0,1,2,4,6
l=[1,2,0,4,0,6,0]
j=0
for i in range(len(l)):
    if l[i]==0:
        l[i],l[j]=l[j],l[i]
        j+=1
print(l)

#order
l=[1,2,0,4,0,6,0]
j=0
A=[]
B=[]
for i in range(len(l)):
    if l[i]==0:
        A.append(l[i])
    else:
        B.append(l[i])
print(A+B)

