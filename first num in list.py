a=[1234,122,1984,29372,100]
i=0
c=[]
while i<len(a):
    b=a[i]
    while b>0:
        r=b%10
        b=b//10
    i=i+1
    c.append(r)
print(c)