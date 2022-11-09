a="aaabbbcccaaaddd"
i=0
b=[]
j=0
while i<len(a):
    if a[i][j] not in b:
        b.append(a[i][j])
    i=i+1
print(b)