# Got it 👍
# Below are **INPUT matrices and EXPECTED OUTPUTS** for **all transpose problems**, **no code**.

# ---

# ## 📥 INPUT MATRIX – A (3×3)

a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# ---

# ## ✅ 1️⃣ Print Transpose of a Square Matrix

# ### 🔹 Expected Output (Transpose of A)
# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[j][i],end=" ")
#     print()
# ```
# 1  4  7
# 2  5  8
# 3  6  9
# ```

# ---

# ## 📥 INPUT MATRIX – B (2×3)

a=[
    [1,2,3],
    [4,5,6],
]
for j in range(len(a[0])):
    for i in range(len(a)):
        print(a[i][j],end=' ')
    print()

# ---

# ## ✅ 2️⃣ Print Transpose of a Rectangular Matrix

# ### 🔹 Expected Output (3×2)

# ```
# 1  4
# 2  5
# 3  6
# ```

# ---

# ## 📥 INPUT MATRIX – C (3×3)

# ```
# 1  2  3
# 2  5  6
# 3  6  9
# ```

# ---

# ## ✅ 3️⃣ Check if Matrix is Symmetric

# ### 🔹 Expected Output

# ```
# True
# ```

# (Matrix is equal to its transpose)

# ---

# ## 📥 INPUT MATRIX – A (same as first)

# ```
# 1  2  3
# 4  5  6
# 7  8  9
# ```

# Transpose:

# ```
# 1  4  7
# 2  5  8
# 3  6  9
# ```

# ---

# ## ✅ 4️⃣ Sum of Transposed Matrix Rows

# ### 🔹 Expected Output

# ```
# Row 0 Sum = 12
# Row 1 Sum = 15
# Row 2 Sum = 18
# ```

# ---

# ## ✅ 5️⃣ Sum of Transposed Matrix Columns

# ### 🔹 Expected Output

# ```
# Column 0 Sum = 6
# Column 1 Sum = 15
# Column 2 Sum = 24
# ```

# ---

# ## 📥 INPUT MATRIX – A

# ```
# 1  2  3
# 4  5  6
# 7  8  9
# ```

# ---

# ## ✅ 6️⃣ Print Upper Triangle Using Transpose Logic

# ### 🔹 Expected Output

# ```
# 1  2  3
#    5  6
#       9
# ```

# ---

# ## ✅ 7️⃣ Convert First Row to Column

# ### 🔹 Expected Output

# ```
# 1
# 2
# 3
# ```

# ---

# ## ✅ 8️⃣ Convert First Column to Row

# ### 🔹 Expected Output

# ```
# 1  4  7
# ```

# ---

# ## 📥 INPUT MATRIX – A

# ```
# 1  2  3
# 4  5  6
# 7  8  9
# ```

# ---

# ## ✅ 9️⃣ Double Transpose Check

# ### 🔹 Expected Output

# ```
# Original Matrix:
# 1  2  3
# 4  5  6
# 7  8  9

# After Double Transpose:
# 1  2  3
# 4  5  6
# 7  8  9

# Result: True
# ```

# ---

# ## ✅ 🔟 Transpose and Reverse Rows

# ### 🔹 Step 1: Transpose

# ```
# 1  4  7
# 2  5  8
# 3  6  9
# ```

# ### 🔹 Step 2: Reverse Each Row

# ### 🔹 Expected Output

# ```
# 7  4  1
# 8  5  2
# 9  6  3
# ```

# ---

# ## 🧠 Key Memory Tip

# Transpose = **swap row & column positions**
# `(i, j)` → `(j, i)`

# ---

# If you want next:
# 👉 **Matrix rotation (90°, 180°) input/output**
# 👉 **Spiral traversal input/output**
# 👉 **Boundary & pattern matrix problems**

# Just tell me 🚀
