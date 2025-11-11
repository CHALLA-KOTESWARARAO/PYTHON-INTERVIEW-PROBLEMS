a=[1,2,3,5,1,5,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)