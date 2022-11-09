a="dularpanndey"
i=0
c=[]
f=[]
while i<len(a):
    b=a.count(a[i])
    if a[i] not in f:
        f.append(a[i])  
        d=a[i]+":"+str(b)
        c.append(d)
    i=i+1
print(c)