a=["p","q"]
i=1
b=[]
while i<=5:
    j=0
    while j<len(a):
        c=a[j]+str(i)
        b.append(c)
        j=j+1
    i=i+1
print(b)