#print fibonacci series
# a,b=0,1
# for i in range(5):
#     print(a,end=" ")
#     a,b=b,a+b

#print non fibonacci series
a,b=0,1
li=[0,1]
for i in range(21):
    a,b=b,a+b
    li.append(a)
    if i not in li:
        print(i,end=' ')
