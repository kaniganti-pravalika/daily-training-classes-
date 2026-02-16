for i in range(65, 69):
    for j in range(65, 69):
        print(chr(i) , end="")
    print()
for i in range(1,5):
    for j in range(1,5):
        if(j>=5-i):
            print("*" , end="")
        else:
            print("" , end="")
    print()
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
       
        if(j==rows//2+1 or i==rows//2+1):
            print("*" , end="")
        else:
            print(" " , end="")
    print()
for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == 5 or i == 1 or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(1, 6):
    for j in range(1, 6):
        if i == j or i + j == 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()
num=int(input("Enter number: "))
n=1
for i in range(1, num+1):
    for j in range(i):
        print(n, end="")
        n+=1
    print()
num=int(input("Enter number: "))

for i in range(num):
    for j in range(i+1):
        print((i+j+1)%2, end="")
    print()

num=int(input("Enter number: "))
for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break
    else:
        print("Prime number")
        break
num=int(input("Enter number: "))
count=0
sum=0
for i in range(1,num+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        
        print(i, end=" ")
        sum=sum+i
        count=count+1
print("\nThe count of prime numbers is: ",count)
print("The sum of prime numbers is: ",sum)

