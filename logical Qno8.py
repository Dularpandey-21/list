binarynumber=[1,0,0,1,1,0,1,1]
a=len(binarynumber)
i=-1
k=0
sum=0
while i>=-a:
    b=binarynumber[i]
    c=b*2**k
    sum=sum+c
    i=i-1
    k=k+1
print(sum)