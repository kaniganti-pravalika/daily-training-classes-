#string methods
text="Python is easy to learn"
result=text.startswith('is easy')
print(result)
#
text='Live and let live'
print(text.split())
gro='Milk;Butter,Bread'
print(gro.split(','))
print(gro.split(';'))
#join 
mylist=["c","java","c++"]
s="->"
print(s.join(mylist))

#sentence
mylist="Cow is a Animal"
fruits=("banana","mango")
s="->"
new_Mylist=mylist.capitalize()
print("Original name:{}\n capetalized name is:{new_mylist}")
print(mylist.title())
print(s.join(fruits))
print(fruits.split(','))