# num1=int(input("enter the 1st number"))
# num2=int(input("enter the 2nd number"))
# num3=int(input("enter the 3rd number"))
# list1=[]
# list1.append(num1)
# list1.append(num2)
# list1.append(num3)
# print(list1)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if (i!=j and j!=k and k!=i):
#                 print(list1[i],list1[j],list1[k])






num1=int(input("enter th 1st number"))
num2=int(input("enter the 2nd number"))
num3=int(input("enter the 3rd number"))
list1=[]
list1.append(num1)
list1.append(num2)
list1.append(num3)
print(list1)
i=0
while i<3:
    j=0
    while j<3:
        k=0
        while k<3:
            if (i!=j and j!=k and k!=i):
                print(list1[i],list1[j],list1[k])
            k=k+1
        j=j+1
    i=i+1