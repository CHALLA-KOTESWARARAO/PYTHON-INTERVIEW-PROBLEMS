# ### 1. **Introduction**:
#    - **Linear Search**: A simple search algorithm that checks each element 
#                        in a list or array sequentially until the target element
#                        is found or the end of the list is reached.
# ### 3. **Example**
#    - **Given Array**: [2, 4, 6, 8, 10]
#    - **Target Element**: 8
#    - **Steps**:
#       - Compare 2 with 8 (not a match).
#       - Compare 4 with 8 (not a match).
#       - Compare 6 with 8 (not a match).
#       - Compare 8 with 8 (match found, return index 3).
def linear_search(li,sear):
    for i in range(len(li)-1):
         if sear==li[i]:
            return i
    return -1
li=[1,2,3,4,5,6,7,8]
sear=5
s=linear_search(li,sear)
if s!=-1:
    print(f'{sear} is found at index {s}')
else:
    print(f'{sear} is not found')

