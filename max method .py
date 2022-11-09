# while loop 
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
while i<len(numbers):
    numbers.pop()
    numbers.pop()
    i=i+1
    print(numbers)
    a=max(numbers)
print("Third max number is",a)