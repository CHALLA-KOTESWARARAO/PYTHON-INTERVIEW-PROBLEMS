#53.Rotate an list
#inp:[1,2,3,4,5]
#2
#op:[4,5,1,2,3]

# def Rotate(li,nu):
#     n=nu%len(li)
#     print(n)
#     return li[n:]+li[:n]
# li=[1,2,3,4,5]
# print(Rotate(li,14))

# a=[1,2,3,4,5]
# n=20%len(a)
# i=0
# while i<n:
#     a.append(a[0])
#     a.pop(0)
#     i+=1
# print(a)

#--------------------------------------------------------------------------
# n=18
# a=[10,20,30,40,50]
# n=n%len(a)
# print(a[n:]+a[:n])
#--------------------------------------------------------------------------
n=3
a=[10,20,30,40,50]
n=n%len(a)
i=0
while i<n:
    a.append(a[0])
    a.pop(0)
    i+=1 
print(a)

















