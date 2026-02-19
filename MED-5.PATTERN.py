#------------------------------------------------------------------------------------------
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 1
# 1 2
# 1 2 3
# 1 2 3 4
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(j,end=' ')
        else:
            print(" " ,end=" ")
    print()
#------------------------------------------------------------------------------------------ 
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# A 
# AB
# ABC
# ABCD

n=4
a=["a","b","c","d"]
for i in range(n):
    for j in range(n):
        if j<=i:
            print(a[j],end=' ')
        else:
            print(" " ,end=" ")
    print()
#------------------------------------------------------------------------------------------ 
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 4 3 2 1
# 4 3 2
# 4 3
# 4
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()
#------------------------------------------------------------------------------------------ 
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 1 1
# 1 2 3
# 1 2 3 6
# 1 2 3 4 10
n=4
for i in range(1,n+1):
    sum=0
    for j in range(1,i+1):
        print(j,end=' ')
        sum+=j
    print(sum,end=" ")
    print()

#------------------------------------------------------------------------------------------ 
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 3
# Output     	: 

#      1
# 1	 2
# 1	2   3
# for i in range(1,2):
#     for j in range(1,6):
#         if j==(5//2)+1:
#             print(i,end=" ")
#         else:
#             print('_',end=" ")
# print()
# for i in range(1,2):
#     for j in range(1,6):
#         if j%2==0:
#             print(i,end=" ")
#         else:
#             print('_',end=" ")

# print()
# for i in range(1,2):
#     for j in range(1,6):
#         if j%2!=0:
#             print(i,end=" ")
#         else:
#             print('_',end=" ")
#     print()

#------------------------------------------------------------------------------------------ 
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 1+
# 12++
# 123+++
# 1234++++
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print('+'*i,end="")
    print()
#-----------------------------------------------------------------------------------------------
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# +1
# ++2
# +++3
# ++++4
for i in range(1,5):
    print('+'*i,end='')
    for i in range(1,i+1):
        print(i,end="")
    print()
for i in range(1,5):
    print('+'*i,i,end='')
    print()

#-----------------------------------------------------------------------------------------------
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# A1
# AB12
# ABC123
# ABCD1234
l="ABCD"
for i in range(1,5):
    print(l[:i],end="")
    for j in range(1,i+1):
        print(j,end='')
    print()
#------------------------------------------------------------------------------------------
# ●	Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# A
# ab
# ABC
# abcd
a='abcd'
for i in range(1,5):
        if i%2==0:
            print(a[:i])
        else:
            print(a[:i].upper())


        