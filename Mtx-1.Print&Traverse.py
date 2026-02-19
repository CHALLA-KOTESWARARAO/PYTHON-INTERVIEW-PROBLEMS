
# ## 🟢 Matrix Print & Traverse – 10 Practice Problems
mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# ### 1️⃣ Print Matrix Row-wise

# Write a program to print all elements of a given matrix **row by row**.
for i in mat:
    for j in i:
        print(j,end=" ")
    print()

# ### 2️⃣ Print Matrix Column-wise

# Write a program to print all elements of a matrix **column by column**.

for i in range(len(mat)):
    for j in range(len(mat)):
        print(mat[j][i],end=" ")
    print()

# ### 3️⃣Print Matrix in Reverse Row Order

# Print the matrix starting from the **last row to the first row**, but elements in each row should remain in the same order.

for i in range(len(mat)-1,-1,-1):
    for j in range(len(mat)):
        print(mat[i][j],end=" ")
    print()

# ### 4️⃣ Print Matrix in Reverse Column Order

# Print the matrix such that each row is printed from **right to left**.

for i in range(len(mat)):
    for j in range(len(mat)-1,-1,-1):
        print(mat[i][j],end=" ")
    print()

