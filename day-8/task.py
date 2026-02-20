n=int(input())
num=list(map(int,input().split(',')))
prod=1
if 7 in num:
    index_of_7=num.index(7)
    if index_of_7==n-1:
        prod=-1
    for i in num[index_of_7+1:]:
        prod*=i
        
else:
    for i in num:
        prod*=i
print(prod)