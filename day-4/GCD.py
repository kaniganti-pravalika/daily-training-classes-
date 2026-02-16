#GCD of two numbers
a=12
b=8
while(b!=0):
    r=a%b
    a=b
    b=r
print("GCD is",a)
#LCM of two numbers
a=12
b=8
x,y=a,b
while(b!=0):
    r=a%b
    a=b
    b=r
gcd=a
lcm=(x*y)//gcd
print("GCD is",gcd)
print("LCM is",lcm)
#GCD and LCM of three numbers
first=20 
second=30
thrid=50
x,y,z=first,second,thrid
while(second!=0):
    r=first%second
    first=second
    second=r
gcd=first
lcm=(x*y)//gcd
Lcm=lcm
while(thrid!=0):
    r=gcd%thrid
    gcd=thrid
    thrid=r
    Gcd=gcd
    Lcm=(Lcm*z)//Gcd
print("GCD is",gcd)
print("LCM is",Lcm)
a=20
b=30
c=30
x=a
y=b 

while(y!=0):
    x,y=y,x%y
gcd_ab=x
lcm_ab=(a*b)//gcd_ab
x=lcm_ab
y=c
while(y!=0):
    x,y=y,x%y
gcd_abc=x
lcm_abc=(lcm_ab*c)//gcd_abc

print("LCM of a and b is",lcm_ab)


