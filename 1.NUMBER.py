#1.find len of number
num=150055
num_len=0
while num:
    num//=10
    num_len+=1
print(num_len)
#2.rev a number
nu=321
rev_num=0
while nu:
    d=nu%10
    rev_num=rev_num*10+d
    nu//=10
print(rev_num)
