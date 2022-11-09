n=int(input("enter the number of rows:"))
i=10
while i<=n*10:
    j=i
    while j>=10:
        print(j,end=" ")
        j=j-10
    i=i+10
    print()