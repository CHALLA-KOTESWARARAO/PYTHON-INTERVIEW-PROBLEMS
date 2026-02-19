# Find Unique Elements
def unique(li):
    i=0
    while i<len(li):
        j=1
        while j<len(li):
            if li[i]==li[j]:
                li.pop(j)
            else:
                j+=1
        i+=1
        
    return li
li=[1, 2, 2, 3, 4, 4, 5]
print(unique(li))