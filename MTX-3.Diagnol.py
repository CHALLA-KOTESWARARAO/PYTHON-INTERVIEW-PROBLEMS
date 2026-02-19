
# ## 📥 INPUT MATRIX (3×3)

# ```
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# ```

# Matrix indices for understanding:

# ```
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
# ```

# ---

# ## ✅ 1️⃣ Print Main Diagonal

# (Main diagonal → i == j)

# ### 🔹 Expected Output

for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            print(a[i][j])


# ---

# ## ✅ 2️⃣ Print Secondary Diagonal

# (Secondary diagonal → i + j = n − 1)

# ### 🔹 Expected Output

for i in range(len(a)):
    for j in range(len(a)):
        if i+j==len(a)-1:
            print(a[i][j])

# ---
# opposite diagnols 
for i in range(len(a)-1,-1,-1):
    for j in range(len(a)-1,-1,-1):
        if i==j:
            print(a[i][j],end=" ")
        else:
            print("*",end=" ")
    print()



for i in range(len(a)-1,-1,-1):
    for j in range(len(a)-1,-1,-1):
        if i+j==len(a)-1:
            print(a[i][j])

# ## ✅ 3️⃣ Sum of Main Diagonal

# ### 🔹 Expected Output
main=0
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            main+=a[i][j] 
print(f'Sum of Main Diagonal {main}')
# ```
# 15
# ```

# (1 + 5 + 9)

# ---

# ## ✅ 4️⃣ Sum of Secondary Diagonal

# ### 🔹 Expected Output
sec=0
for i in range(len(a)):
    for j in range(len(a)):
        if i+j==len(a)-1:
            sec+=a[i][j] 
print(f'Sum of Secondary Diagonal {sec}')
# ```
# 15
# ```

# (3 + 5 + 7)



# ## ✅ 6️⃣ Print Both Diagonals

# (Main diagonal first, then secondary diagonal)
print("---------------------------------------------------------")
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            print(a[i][j],end=" ")
        elif i+j==len(a)-1:
            print(a[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# ## ✅ 7️⃣ Count Even Elements on Main Diagonal

# ### 🔹 Expected Output

# ```
# 0
# ```

# (Main diagonal elements are 1, 5, 9 → all odd)

# ---

# ## ✅ 8️⃣ Count Odd Elements on Secondary Diagonal

# ### 🔹 Expected Output

# ```
# 3
# ```

# (3, 5, 7 → all odd)

# ---

# ## ✅ 9️⃣ Check Diagonal Equality

# (Main diagonal sum == Secondary diagonal sum)

# ### 🔹 Expected Output

# ```
# True
# ```

# ---

# ## ✅ 🔟 Print Non-Diagonal Elements

# (Exclude both diagonals)

# ### 🔹 Expected Output

# ```
# 2  4  6  8
# ```
for i in range(len(a)):
    for j in range(len(a)):
        if i==j or i+j==len(a)-1:
            print("*",end=" ")
        else:
            print(a[i][j],end=' ')
    print()
# ---

# ## 🧠 Golden Diagonal Rules (Remember Forever)

# * **Main diagonal** → `i == j`
# * **Secondary diagonal** → `i + j == n - 1`
# * Center element in odd matrix belongs to **both diagonals**

# ---

# If you want next:
# 👉 **10 diagonal problems with 4×4 matrix**
# 👉 **Advanced diagonal + pattern problems**
# 👉 **Spiral matrix input/output**
# 👉 **Interview tricky diagonal questions**

# Just tell me 🚀
