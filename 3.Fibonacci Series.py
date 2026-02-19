# print fibonacci series
a,b=0,1 
for i in range(5):
    print(a,end=" ")
    sum=a+b 
    a,b=b,sum
    
