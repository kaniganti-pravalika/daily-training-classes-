print("Hello")
print("GM")
#print(10/0)#ZeroDivisionError: division by zero
print("How are You?")

try:
    print("Hello")
    print(10/0)
except ZeroDivisionError as msg:
    print(type(msg))#<class 'ZeroDivisionError'>
    print(msg.__class__)
    print(msg)
    print(msg.__class__,__name__)#<class 'ZeroDivisionError'> __main__

#try with multiple except blocks
'''try:
    X=int(input("Enter the X value:"))
    Y=int(input("Enter the Y value:"))
    print("The Result:",X/Y)
except ZeroDivisionError:
    print("We cannot divide by Zero")
except ValueError:
    print("Please provide the int values")
print("out side")
'''
#finally
try:
    try:
        print("Z")
    except:
        print("Y")
    print("A")
    print(10/0)
    print("E")
except:
    print("B")

else:
    print("D")
finally:
    print("C")

#nested try
try:
    #print(10/0)
    try:
        #print(20/0)
        print("Z")
        print(10/0)
    except:
        print(10/0)
        print("Y")
        print(10/0)
    else:
        print("X")
    finally:
        print(10/0)
    print(10/0)
    print("A")
    print(10/0)
    print("E")
    print(10/0)

except:
    #print(10/0)
    print("B")
    #print(10/0)

else:
    print(10/0)
    print("D")
    print(10/0)
finally:
    print("C")

#creating own exception
'''class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
age=int(input("Enter Age:"))
if age>60:
    raise TooYoungException("Please a wait for some time you get best match ")#TooYoungException: Please a wait for some time you get best match 

elif age<18:
    raise TooOldException("your age is crossed no chance")#TooOldException: your age is crossed no chance

else:
    print("You will get match details soon by email ")'''

try:
    print("hello")

finally:
    print("hello")
print("hye")
