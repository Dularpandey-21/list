a="ArchAnA"
i=0
b=[]
while i<len(a):
    if a[i].isupper()==True:
        b.append(i)
    i=i+1
print(b)



l=["archana","aariya"]
l1=["singh","pandey"]
i=0
c=[]
while i<len(l):
    b=l[i][0].upper()+l1[i][0].upper()
    c.append(b)
    i=i+1
print(c)
    
