a=[1,2,3,4,5,6]
b=[]
i=0
j=-1
while i<len(a)//2:
    b.append(a[j])
    b.append(a[i])
    j=j-1
    i=i+1
print(b)