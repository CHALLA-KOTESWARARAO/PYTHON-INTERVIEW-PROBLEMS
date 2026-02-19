#find 1000 's & 500's in  number 

a=200
ans=a//1000  #1000
a=a%1000 #remaining
print(ans)
b=a//500  #500
a=a%500 #remaining
print(b)
print(a) 




# a='400' 
# ks=0  
# _500s=0 
# remaining=0
# if len(a)>3:
#     ks=a[0:-3] 
# if len(a)>2:
#     if a[-3]=='5':
#         _500s=1
#     else:
#         remaining=a[-3:]
# print(ks,_500s,remaining)

# 0 2 0 4 0  3 2 0 5 7 0 2 0 3 

# 2 4 5 12 2 3 

