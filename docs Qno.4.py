a=[6,1,3,5,6,3,1]
i=0
pro=1
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
j=0
while j<len(b):
    pro=pro*a[j]
    j=j+1 
print(pro)