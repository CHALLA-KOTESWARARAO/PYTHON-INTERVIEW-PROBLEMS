#30. Calculate the GCD (Greatest Common Divisor) of two numbers
a, b = 48,18
x, y = a, b      # Step 1: Initialize values

# Step 2: Apply Euclidean Algorithm
while y:            # repeat until remainder is 0
    x, y = y, x % y # update values

print(f"GCD of {a} and {b} is: {x}")

# **Q: What is LCM?**

# * The **GREATEST Common Divisor** of two numbers is the Largest number that divides both numbers exactly
# GCD OF 12 AND 18 IS 6,
#because 6 divides both 12 and 18