l=list(map(int, input("enter the elements of list:").split()))
value=int(input("enter the value to remove:"))
while value in l:
    l.remove(value)
print(l)
