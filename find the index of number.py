a=[1,2,3,4,5]
b=int(input("enter the number"))
i=0
while i<len(a):
    if b==a[i]:
        print("number=",b,"index of num=",i)
        break
    i=i+1
else:
    print("not in list")