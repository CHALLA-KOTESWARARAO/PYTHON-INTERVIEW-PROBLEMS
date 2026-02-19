# #moves zeros to end
# a=[0,7,7,7,5,0,7,0,9]
# # z=[]
# # nor=[]
# # for i in a:
# #     if i==0:
# #         z.append(i)
# #     else:
# #         nor.append(i)
# # print(nor+z)
# x=0
# for i in range(len(a)-1):
#     if a[x]==0:
#         a.append(a[x])
#         a.pop(x)

#     else:
#         x+=1
# print(a)
a=[1,2,3,4,5]
i=0
x=0
while i<len(a):
    if a[x]%2==0:
        a.append(a[x])
        a.pop(x)
        i+=1
    else:
        x+=1
    i+=1
print(a)
