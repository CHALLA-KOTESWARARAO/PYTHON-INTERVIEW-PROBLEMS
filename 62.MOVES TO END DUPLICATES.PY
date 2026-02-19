a=[1,1,5,1,2,9,6,5,2,1,8,6,8]
i=0
k=0
le=len(a)
jle=len(a)
p1=i
while i<le:
    p2=i+1
    j=i+1
    while j<jle:
        if a[p1]==a[p2]:
            a.append(a[p2])
            a.pop(p2)
            jle-=1
            k+=1
        else:
            p2+=1
        j+=1
    if a[i] in a[i+1:]:
        a.append(a[p1])
        a.pop(p1)
        k+=1
    else:
        i+=1
    if k==len(a):
        break
print(a)