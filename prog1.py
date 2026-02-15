marks=int(input("enter the marks :"))
atte=float(input("enter the attendance percentage :"))
disc=int(input("enter the disciplane score(0-10) :"))
if(marks>=0 and marks<=100):
    if(marks>=90):
        grade="A"
    elif(marks>=75 and marks<90):
        grade="B"
    elif(marks>=60 and marks<75):
        grade="C"
    elif(marks<60):
        grade="fail"
    def downgrade(g):
        grade_order=['A','B','C','fail']
        if(g in grade_order and grade!='fail'):
            return grade_order[grade_order.index(g)+1]
        return g
    if(atte<75):
        grade=downgrade(grade)
    if(disc<5 and grade in['A','B']):
        grade=downgrade(grade)
    if(marks>95 and atte>90):
        print("outstanding student")
    print("final grade :",grade)
else:
    print("invalid input") 