n=int(input("enter the number of students:"))
d={}
for i in range(n):
    name=input("enter the name of the student:")
    marks=int(input("enter the marks of student:"))
    d[name]=marks
while True:
    name=input("enter the name of student to get their marks:")
    marks=d.get(name,-1)
    if(marks==-1):
        print("student is not found!")
    else:
        print("the student",name,"marks are",marks)
    option=input("do you want to check marks of any other student ?(yes/no)")
    if option=="no":
        break
print("thank you for using the application!")
