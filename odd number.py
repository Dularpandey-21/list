list1=[23,45,32,25,46,33,71,90]
i=0
a=[]
while i<len(list1):
    if list1[i]%2!=0:
        a.append(list1[i])
    i=i+1
print("Odd number=",a)