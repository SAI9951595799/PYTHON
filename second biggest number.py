numbers=[]
for x in range(3):
    num=int(input(f"enter the numbers {x+1}:"))
    numbers.append(num)
numbers.sort()
print(numbers[1])
