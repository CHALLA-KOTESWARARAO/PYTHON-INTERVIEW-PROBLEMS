#Reverse order of words
a='I love Python'
li=[]
b=' '
for i in range(len(a)-1):
    if a[i]!=" ":
        b+=a[i]
        if len(a)-1==i:
            li.append(b)
            b+=''
    else:
        li.append(b)
        b+=''
print(li)
# for i in a:
#     if i !=" ":
#         b+=i
#         if len(a)-1==a.index(i):
#             li.append(b)
#             b=''
#     else:
#         li.append(b)
#         b=''
# print(li)

