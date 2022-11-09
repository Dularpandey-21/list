# a=[1,5,4,6,8]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)



# a=[5,4,6,8,2,3,1,7]
# i=0
# while i<len(a)-1:
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         j=j+1
#     i=i+1
# print(a)


a=[1,2,3,4,5,6]
b=[]
i=1
while i<len(a)+1:
    c=a[-i]
    b.append(c)
    i=i+1
print(b)

# x=int(input("enter the number"))
# y=int(input("enter the number"))
# i=1
# while 