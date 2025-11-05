n=int(input("enter the count of numbers:"))
numbers=[]
for i in range(n):
    num=int(input("enter the number one by one{i+1}:"))
    numbers.append(num)
    if(n%2==0):
        print("this number is even!")
        
 else:
 print("this number is odd!")
