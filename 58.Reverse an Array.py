# Reverse an Array
def rev_array(lis):
    l=[]
    for i in range(len(lis)-1,-1,-1):
        l.append(lis[i])
    return l
lis=[1, 2, 3, 4, 5]
print(rev_array(lis))