# while loop 
l=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
i=0
a=[]
while i<len(l)-2:
    b=l[i],l[i+1],l[i+2]
    a.append(list(b))
    i=i+3
print(a)