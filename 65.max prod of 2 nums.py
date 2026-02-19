# ●	Find the Maximum Product of Two Elements

# Problem: Write a function to find the maximum product of two elements in an array.
# Testcase 1:
# Input: [3, 5, -2, 8, 11]
# Output: 8 * 11 → 88
def max_prod(a):
    f=float("-inf")
    s=float("-inf")
    for i in a:
        if i>f:
            s=f
            f=i 
        elif i>s and i!=f:
            s=i
    print(f,s)
    return f*s 
print(max_prod([22,3, 5, -2, 8, 11]))

# a = [11, 2, 5, 8, 9]

# f = float("-inf")
# s = float("-inf")

# for i in a:
#     if i > f:
#         s = f
#         f = i
#     elif i > s and i != f:
#         s = i

# print(f, s)
