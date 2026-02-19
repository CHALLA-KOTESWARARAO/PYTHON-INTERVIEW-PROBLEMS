a=[1,2,3,4,5]
i=0
j=3
max_len=0
while j<=len(a):
    su=sum(a[i:j])
    if su>max_len:
        max_len=su
    i+=1
    j+=1
print(max_len,i,j)
