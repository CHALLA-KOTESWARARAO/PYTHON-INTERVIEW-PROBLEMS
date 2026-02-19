# ●	Write a program that takes array of numbers are input, 
# print the second duplicate number and it’s occurrence.
# a=[ 64, 1, 7, 1, 2,2] 
a=[ 121, 8, 1, 4, 5, 4, 8, 1 ]
def sec_occ(a):
    nu=0
    num=0
    occ=1
    for i in range(len(a)-1):
        if a[i] in a[i+1:] and occ==2:
            for j in a:
                if j==a[i]:
                    nu+=1
                    num=j
            return nu,num
        elif a[i] in a[i+1:]:
            occ+=1
print(sec_occ(a))