# while loop 
l=[9119]
i=0
while i<len(l):
    n=l[i]
    j=0
    while j<n:
        r=n%10
        t=r*r
        n=n//10
        print(t,end="")
        j=j+1
    i=i+1