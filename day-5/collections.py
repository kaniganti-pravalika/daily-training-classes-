#creating a list 
''''from email.mime import text


a=[]
b=("")
print(type(a),type(b))
#list  inbuilt functions
a=["ramesh","Ashvini",True,"Asif","Asif",[False,1,2,3]]
print(a)
#length of list
fruits=["apple","banana","grapes"]
print(len(fruits))
#max
numbers=[1,2,3,4,5]
print(max(numbers))
months=["January","February","December"]
#sorting decending order
nums=[3,1,5,2]
print(sorted(nums,reverse=True))

#any()
x=[1,3,4,0]
print(any(x))

#all
y=[1,3,4,0]
print(all(y))

#list ibuilt methods
#append
animals=["dog","cat","rabbit"]
wild_animals=["lion","tiger"]
animals.append("wild animals")
print(animals)
#neated indexing
animals=["dog","cat","rabbit"]
wild_animals=["tiger",'fox']
animals.append(wild_animals)
print(animals[3])
print(animals[3][0])
print(animals[3][0][0])
print(animals[3][1][0])

#problem
n=input("enter a alphanumeric string:")
num=[]
if n.isalnum():
    for i in n:
        if i.isdigit():
            num.append(i)
print(num)
#another approach
n=input("enter a alphanumeric string:")
num=[]
for x in n:
    if x in "0123456789":
        num.append(x)
print(num)
#extend
a=[1,2,3]
a.extend([4,5,6])
print(a)'''
#


