a=[
    [5,4,9],
    [8,7,6],
    [1,2,3]
]

# ---

# ## 🟢 Matrix Row / Column Sums – 10 Practice Problems

# ### 1️⃣ Sum of All Elements

# Given a matrix, find the **sum of all elements** present in the matrix.
# sum=0
# for i in a:
#     for j in i:
#         sum+=j 
# print(sum)

# ### 2️⃣ Row-wise Sum

# Print the **sum of elements in each row** of the matrix.
# for i in a:
#     sum=0 
#     for j in i:
#         sum+=j 
#     print(sum)

# ### 3️⃣ Column-wise Sum

# Print the **sum of elements in each column** of the matrix.
# for i in range(len(a)):
#     sum=0
#     for j in range(len(a)):
#         sum+=a[j][i]
#     print(sum)


# ### 4️⃣ Find Row with Maximum Sum

# Find the **row index** which has the **maximum sum** of elements.
# li=[]
# for i in a:
#     sum=0
#     for j in i:
#         sum+=j
#     li.append(sum)   
# ind=0 
# ele=0
# for ii in range(len(li)):
#     if li[ii]>ele:
#         ele=li[ii]
#         ind=ii 
# print(li)
# print(ind)


    
    


# ### 5️⃣ Find Column with Minimum Sum

# Find the **column index** which has the **minimum sum** of elements.
# li=[]
# for i in range(len(a)):
#     sum=0
#     for j in range(len(a)):
#         sum+=a[j][i]
#     li.append(sum)
# ind=0 
# ma=0 
# for i in range(len(li)):
#     if li[i]>ma:
#         ma=li[i]
#         ind=i
# print(li,ind)


# ### 6️⃣ Check Equal Row Sums

# Check whether **all rows have the same sum**.
# Print `True` or `False`.

# ---

# ### 7️⃣ Difference Between Row Sums

# Print the **difference between the maximum row sum and minimum row sum**.

# a=[
#     [5,4,9],
#     [8,7,6],
#     [1,2,3]
# ]
# lis=[]
# max=float('-inf')
# min=float('inf')
# for i in a:
#     sum=0
#     for j in i:
#         sum+=j 
#     lis.append(sum)
#     if sum>max:
#         max=sum
#     if sum<min:
#         min=sum
# print(lis,max-min)


# ### 8️⃣ Sum of Even Numbers Row-wise

# For each row, calculate the **sum of only even numbers**.
# for i in a:
#     sum=0
#     for j in i:
#         if j%2==0:
#             sum+=j 
#     print(sum)


# ### 9️⃣ Sum of Odd Numbers Column-wise

# For each column, calculate the **sum of only odd numbers**.

# for i in range(len(a)):
#     sum=0
#     for j in range(len(a)):
#         if a[j][i]%2==0:
#             sum+=a[j][i]
#     print(sum)
# ### 🔟 Compare Row Sum and Column Sum

# For each index `i`, compare:

# * sum of **row i**
# * sum of **column i**

# Print whether they are **equal or not**.

for i in range(len(a)):
    row_sum=0
    column_sum=0
    for j in range(len(a)):
        row_sum+=a[i][j]
        column_sum+=a[j][i] 
    if row_sum==column_sum:
        print(f"{row_sum,column_sum} are equal")
    else:
        print(f"{row_sum,column_sum} are not equal")


