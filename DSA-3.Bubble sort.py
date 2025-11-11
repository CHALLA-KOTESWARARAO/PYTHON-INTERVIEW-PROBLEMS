li=[5,2,7,9,4,3,1]
for i in range(len(li)-1):
    for j in range(len(li)-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)

