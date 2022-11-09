list=[34.67,12,-94.89,0,'python','C#']
i=0
while i<len(list):
    list.remove(list[i])
    list.pop()
    i=i+1
print(list)