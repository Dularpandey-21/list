a=["aariya","rukshar","muskan","juli"]
i=0
c=[]
while i<len(a):
    if i==2:
        c.append(a[i][0])
        print(c)
    c.append(a[i][-1])
    i=i+1
print(c)