#29. Calculate the LCM (Least Common Multiple) of two numbers.

a, b = 15,50
x, y = a, b      # Step 1: Initialize values

# Step 2: Apply Euclidean Algorithm
while y:            # repeat until remainder is 0
    x, y = y, x % y # update values

# Step 3: x now contains gcd
lcm = (a * b) // x  # apply formula

print(f"LCM of {a} and {b} is: {lcm}")










# Perfect ✅ Let me give you a **step-by-step explanation** you can use directly in an interview:

# ---

# ### 🔹 Step-by-Step Explanation of LCM Code

# **Q: What is LCM?**

# * The **Least Common Multiple** of two numbers is the smallest number that is divisible by both.
# * Formula:



#   $$
#   LCM(a, b) = \frac{a \times b}{GCD(a, b)}
#   $$

# ---

# **Q: How do you find GCD?**

# * We use the **Euclidean Algorithm**:

#   * `gcd(a, b) = gcd(b, a % b)`
#   * Repeat until `b = 0`.
#   * At that point, `a` is the gcd.

# ---

# **Q: Walk me through the code.**

# ```python
# a, b = 15, 50

# # Step 1: Initialize values
# x, y = a, b

# # Step 2: Apply Euclidean Algorithm
# while y:            # repeat until remainder is 0
#     x, y = y, x % y # update values

# # Step 3: x now contains gcd
# lcm = (a * b) // x  # apply formula

# print(f"LCM of {a} and {b} is: {lcm}")
# ```

# ---

# **Q: What happens for 15 and 50?**

# 1. Start: `x=15, y=50`
# 2. Step 1: `x=50, y=15`
# 3. Step 2: `x=15, y=5`
# 4. Step 3: `x=5, y=0 → gcd=5`
# 5. Apply formula:

# ✅ Answer: `150`

