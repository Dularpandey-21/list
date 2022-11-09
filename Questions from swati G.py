# names=["Swathi","Aariya","Archana","Anjali","Jain","Ratua"]
# room=[1,2,3]
# i=0
# j=0
# while j<len(room):
#     print("room",room[j])
#     print("1.",names[i])
#     print("2.",names[i+1])
#     j=j+1
#     i=i+2
          
          
          
          
a="Aariya is singing very loudly"
i=0
b=""
while i<len(a):
    if a[i]!="i" or a[i]!="s":
        b=b+a[i]
    i=i+1
print(b)
a="Aariya is singing very loudly"
i=0
b=a.split()
c=""
while i<len(b):
    if b[i]!="singing":
        c=c+b[i]+" "
    i=i+1
print(c)