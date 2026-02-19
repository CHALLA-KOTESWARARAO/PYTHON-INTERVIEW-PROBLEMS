# Write a program that takes array of numbers as input, among the numbers in array, check how many numbers starts with the same digit and ends with the same digits. Print the count of such kind of numbers in the given array.

# Testcase1	:  [ 34, 88, 423, 121, 2382, 10]
# Output     	:  3
# Explanation : In the given array of number [ 34, 88, 423, 121, 2382, 10], the numbers 88, 121 and 2382 started with same digit and ended with the same digit. The count is 3.
# Testcase1	:  [ 102, 56, 42, 11, 64, 10]
# Output     	:  1
def samedigit(li):
    count=0
    for i in li:
        a=str(i)
        if a[0]==a[len(a)-1]:
            count+=1
    return count 
print(samedigit([ 102, 56, 42, 11, 64, 10]))