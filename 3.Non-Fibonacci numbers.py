#print non fibonacci series
a,b=0,1
fib=[0,1]
NonFib=[]
for i in range(21):
    a,b=b,a+b
    fib.append(a)
    if i not in fib:
        NonFib.append(i)
print(NonFib)
        
