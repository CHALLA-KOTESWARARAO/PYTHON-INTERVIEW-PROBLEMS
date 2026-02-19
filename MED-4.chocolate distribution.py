a=[3,4,1,9,56,7,9,12]
a.sort()
m=5
mav=float('inf')
mav_array=[]

print(a)
for i in range(len(a)):
    v=[]
    ma=0
    if len(a)>=m+i:
        v=a[i:m+i]
        print(v)
        ma=max(v)-min(v)
    else:
        break
    if ma<mav:
        mav=ma
        mav_array=v
print(mav,mav_array)
