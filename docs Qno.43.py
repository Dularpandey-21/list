# while loop 
l=[1,3,4,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
i=4
while i<len(l):
    l.insert(i,20)
    i=i+5
print(l)