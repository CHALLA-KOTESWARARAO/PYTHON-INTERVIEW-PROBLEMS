a=[1,2,3,5,1,5,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

#2 pointers
c=[1,2,3,5,1,5,8]
x=0
for j in range(len(c)-1):
    y=x+1
    for j in range(len(c)-1):
         if a[x]==a[y]:
            a.pop(y)
         else:
            y+=1
print(c)
