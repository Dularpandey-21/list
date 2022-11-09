l=[2,-7,5,-64,-14]
pos=0
neg=0
for i in l:
    if i>0:
        pos=pos+1
    else:
        neg=neg+1
print("Total positive number=",pos)
print("Total negative number=",neg)