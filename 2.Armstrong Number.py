# num2=256
# num1=num2
# num=num1
# num_len=0
# while num:
#     num=num//10
#     num_len+=1

# arm=0
# while num1:
#     d=num1%10
#     arm+=d**num_len
#     num1//=10
# print("armstrong" if arm==num2 else "not armstrong") 

a=121
le=len(str(a))
arm=0
while a:
    n=a%10 
    arm+=n**le 
    a//=10 
print(arm)