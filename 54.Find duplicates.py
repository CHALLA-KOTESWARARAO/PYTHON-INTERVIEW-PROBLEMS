a=[1,2,3,5,1,5,8]
dup=[]
for i in range(len(a)-1):
    if a[i] in a[i+1:]:
        dup.append(a[i])
print(dup)