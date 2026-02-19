# 1.FIND LEN OF A NUMBER
num=12345
len=0 
while num:
    len+=1
    num=num//10
print(len)
#reverse a number
num=12345
rev=0
while num:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

