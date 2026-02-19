# ●	Intersection of Two Arrays

# Problem: Write a function that returns the common elements between two arrays.
# Testcase 1:
# Input: [1, 2, 3], [2, 3, 4]
# Output: [2, 3]
def intersec(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c 
print(intersec([1, 2, 3,4], [2, 3, 4]))