''''for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*  ", end="")
        else:
            print("   ", end="")
    print()

sum=0
for n in range(1, 11):
    sum=sum+n
    
print(sum)
a=int(input("Enter the number: "))
sum=0
while(a>0):
    if(a%2==0):
        digit=a%10
        sum=sum+digit
        a=a//10
    else:
        a=a//10
print("The sum of the digits is: ",sum)
a=int(input("Enter the number: "))
prod=1
while(a>0):
    if(a%2==1):
        digit=a%10
        prod=prod*digit
        a=a//10
    else:
        a=a//10
print("The product of the odd numbers is: ",prod)
a=int(input("Enter the number: "))
count=0
while(a>0):
    count=count+1
    a=a//10
    
print("The count of even digits is: ",count)
a=int(input("enter a value:"))
rev=0
while(a>0):
    digit=a%10
    rev=rev*10+digit
    a=a//10
print("The reverse of the number is: ",rev)
num=int(input("Enter the number: "))
rev=''
for i in range(len(str(num))):
    rev=str(num)[i]+rev
print("The reverse of the number is: ",rev)'''



