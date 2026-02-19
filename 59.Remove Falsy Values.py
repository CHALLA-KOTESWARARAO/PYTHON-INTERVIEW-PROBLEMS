# Remove Falsy Values 
def remove_falsy(lis):
    li=[]
    for i in lis:
        if i:
            li.append(i)
    return li
lis=[0, 1, False, 2, '', 3]
print(remove_falsy(lis))

    
