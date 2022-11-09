a=[1,2,3,4,5]
i=0
largest=0
smallest=a[i]
while i<len(a):
    num=a[i]
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
    i=i+1
print(largest,"it is largest number")
print(smallest,"it is smallest number")