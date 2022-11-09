# a="aariya 1234 @ navgurukul"
# i=0
# while i<len(a):
#     print(a[8:11])
#     i=i+1
#     break



a=[1,2,3,4,5]
b=int(input("enter the number"))
i=0
while i<len(a):
    if b==a[i]:
        print("number=",b,"number of index=",i)
        break
    i=i+1
else:
    print("not in list")