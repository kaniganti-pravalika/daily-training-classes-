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
new_Mylist="Cow is a A9nimal and Parrot is a Bird "
fruits=("banana","mango")
number=(123,5.56998765,987654)
s="->"
Mylist=new_Mylist.capitalize()
print("Original name:{new_Mylist}\n capetalized name is:{Mylist}")#Capitalize the First elements in the Statement 
print(new_Mylist.lower())#converting the all the elements to lower
print(new_Mylist.upper())#converting the all the elements to upper
print(new_Mylist.swapcase())#swaping the elements lower to upper and vice varsa
print(Mylist.title())#Capitalize the First element in the word in the sentence
print(new_Mylist.isupper())# checking the element is upper or not
print(new_Mylist.islower())# checking the element is lower or not
print(new_Mylist.isalpha())
print(new_Mylist.isdigit)
#print(fruits.isdecimal())
print(new_Mylist.isalnum())
print(number.isnumeric())
print(fruits.isspace())
print(new_Mylist.startswith("is"))
print(fruits.index("n"))
print(new_Mylist.find("ngo"))
print(fruits.rfind())
print(new_Mylist.count())
print(fruits.replace("guava"))
print(new_Mylist,fruits.strip())
print(fruits.split())
print(s.join(fruits))
