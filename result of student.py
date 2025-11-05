name=input("enter the name of the student:")
n=int(input("enter the no of subjects:"))
marks=[]
for x in range(n):
    m=int(input("enter the marks of student:"))
    marks.append(m)
    total=sum(marks)
    avg=total/n
result='pass'
for m in marks:
    if(m<35):
        result='fail'
print('name of the student:',name)
print('no of subjects:',n)
print('total marks:',total)
print('average of marks:',avg)
print('result of student:',result)
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)
