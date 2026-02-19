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

def arm(num):
    le=len(str(num))
    onum=num
    arm=0
    while num:
        d=num%10
        arm+=d**le 
        num//=10
    if onum==arm:
        return f"{onum} is armstrong"
    return f"{onum} is not strong"
print(arm(252))