list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
index=0
while index<len(list):
    index=index+1
max=max(list)
print((len(max),max))
list.remove(max)
min=min(list)
print((len(min),min))