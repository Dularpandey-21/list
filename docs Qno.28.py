list=[1,1,2,3,4,5,2,1]
i=0
while i<len(list):
    i=i+1
list.remove(list[0])
list.remove(list[0])
list.pop()
print(list)