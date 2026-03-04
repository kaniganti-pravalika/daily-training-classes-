# bubble sorting
'''l=[5,4,3,2,1]
for i in range (len(l)):
    for j in range(0,len(l)-1-i):#i is for optimization
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            print(l)'''

#insertion sorting
l=[5,4,3,2,1]
for i in range (1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)