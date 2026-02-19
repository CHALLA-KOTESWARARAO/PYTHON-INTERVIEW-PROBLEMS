# Write a program that takes a number as input, print the sum of duplicate numbers in the given number.

# Testcase1	:  7473183
# Output     	:  10
# Explanation	: In the given number 747383, duplicate digits are 7 and 3 because they occurred more than once in the number. So the sum of 7 and 3 are 10.

# Testcase1	:  234234
# Output     	:  9
# Explanation	: In the given number 234234, duplicate digits are 2, 3 and 4 because they occurred more than once in the number. So the sum of 2, 3 and 4 are 9.
a='7473183'
b=list(a)
c=[]
sum=0
for i in b:
    if i not in c:
        c.append(i)
    else:
        sum+=int(i)
print(sum)



