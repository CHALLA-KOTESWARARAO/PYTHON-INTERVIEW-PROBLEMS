lis=[1]
sr=1
def bin_Ser(lis,sr):
    low=0
    high=len(lis)-1
    while low<=high:
        mid=(low+high)//2
        if lis[mid]==sr:
               return mid
        else:
            if sr<lis[mid]:
                high=mid-1
            else:
                low=mid+1
    return -1
a=bin_Ser(lis,sr)
if a!=-1:
     print(f'{sr} is found at index {a}')
else:
     print(f'{sr} is not found')