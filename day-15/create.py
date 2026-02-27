'''
# creating a file
file=open("mytext.txt","w")
file.close()
print("file created successfully!")
#creating file and write greeting
with open("greeting.txt","w") as file:
    file.write("Good Morning!")
print("Greeting file created successfully!")
#creating folder
import os
os.mkdir("MyFolder")'''

#creating file inside that folder
with open("MyFolder/inside.txt","w") as file:
    file.write("this is the inside my folder")
print("Folder and file created Successfully!")
'''import os #disered location
location=r"C:\Users\Pravalika kaniganti\Desktop\daily-training-classes\MyFolder"
os.makedirs(location,exist_ok=True)
file_path=os.path.join(location,"inside.text")

with open(file_path,"w") as file:
    file.write("stored in desired location!")
print("Folder and file created at disred location Successfully!")'''

#problem 
import os
#create your desktop path
desktop_path=r"C:\Users\Pravalika kaniganti\Desktop\daily-training-classes\MyFolder"
#create folder "paragraphanalyser"
Project_folder=os.path.join(desktop_path,"paragraphAnalyser")
os.makedirs(Project_folder,exist_ok=True)
#file path
file_path=os.path.join(Project_folder,"paragraph.txt")
#take paragraph input
print("past or type your paragraph below:\n")
text=input()

#save paragraph to file
with open (file_path,"w",encoding="uft-8") as file:
    file.write(text)
print("\n paragraph saved successfully")
print("stored at:",file_path)

#read file and analyze
with open(file_path,"r",encoding="utf-8") as file:
    content=file.read()
total_characters=len(content)
alphabet_count=0
digit_count=0
special_count=0
for ch in content:
    if ch.isalpha():
        alphabet_count+=1
    elif ch.isdigit():
        digit_count+=1
    elif not ch.isspace():
        special_count+=1
#display Results
print("\n=====ANALYSIS RESULT====")
print("Total characters:",total_characters)
print("Alphabets:",alphabet_count)
print("digits",digit_count)
print("special:",special_count)