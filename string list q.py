# a=['a','b','c','d','e']
# b=['b','e','g','c']
# i=0
# d=[]
# while i<len(a):
#     if a[i] not in b:
#         d.append(b[i])
#     i=i+1
# print(d)


# a=[6,9]
# index=0
# count=0
# i=a[index]
# v=[]
# while i<=max(a):
#     n=a[index]
#     if n==i:
#         v.append(n)
#         index+=1
#     else:
#         count+=1
#         v.append(i)
#     i=i+1
# print(v)



# a=[9,1]
# i=min(a)
# v=[]
# while i<=max(a):
#     n=max(a)
#     if n==i:
#         v.append(n)
#     else:
#         v.append(i)
#     i=i+1
# print(v)



# a=["a","b,","c","d","e","f","g","h","i","j","k","l","m","n"]
# i=0
# c=[]
# while i<3:
#     j=i
#     b=[]
#     while j<len(a):
#         num=a[j]
#         b.append(num)
#         j=j+3
#     i=i+1
#     c.append(b)
# print(c)



a="my name is aariya"
i=0
while i<len(a):
    if a[i]==" ":
        print("-",end="")
    else:
        print(a[i],end="")
    i=i+1