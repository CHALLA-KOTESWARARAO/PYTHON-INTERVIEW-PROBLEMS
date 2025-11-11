'''A Perfect number is a postive integer that is equal
to the sum of its proper divisors(that is all its divisiors excluding itself)
ex: num=6
divisors of 6=1,2,3,6
proper divisors=1+2+3=6
so 6 is a Perfect number
'''
n=6
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print(f"{n} is perfect number" if n==sum else f"{n} is not perfect number")