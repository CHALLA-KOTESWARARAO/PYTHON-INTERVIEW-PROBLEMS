a=[10,7,8,9,18,6,3,4,1,2,5,7]
print(a)
i=0
x=0
ele=0
while i<len(a):
    if a[x]%2==0:
        a.append(a[x])
        a.pop(x)
        ele+=1
    else:
        x+=1
    i+=1
print(a)
a[-ele:]=sorted(a[-ele:]) 
print(a)
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j]%2==0 and a[j+1]%2==0:
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
# print(a)
