# Check if Array is Sorted
def sort(lis):
    nu=lis[0]
    des=True
    for i in lis:
        if i==nu:
            nu+=1
        else:
            des=False
            break
    return des
lis=[5,6]
print(sort(lis))
