#53.Rotate an list
#inp:[1,2,3,4,5]
#2
#op:[4,5,1,2,3]
a=[1,2,3,4,5,6,7,8,9]
b=[]
c=[]
for i in range(2):
    if i<2:
        b.append(a[i])
    else:
        c.append(a[i])
c.extend(b)
print(c)