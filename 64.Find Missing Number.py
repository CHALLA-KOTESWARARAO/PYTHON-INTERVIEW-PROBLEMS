# ●	Find Missing Number

# Problem: Given an array of consecutive numbers with one missing, find the missing number.
# Testcase 1:
# Input: [1, 2, 4, 5]
# Output: [3]
def missing_num(a):
    c=[]
    for i in range(a[0],a[-1]+1):
        if i not in a:
            c.append(i)
    return c 
print(missing_num([1, 2, 4, 10]))
