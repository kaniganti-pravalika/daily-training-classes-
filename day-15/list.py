l=[1,2,3,4,5]
p=[0]*len(l)
s=[0]*len(l)
p[0]=l[0]
for i in range(1,len(l)):
    p[i]=l[i]+p[i-1]
s[len(l)-1]=l[len(l)-1]
for j in range(len(l)-2,-1,-1):
    s[j]=l[j]+s[j+1]
print(p)
print(s)