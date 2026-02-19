
# ## 🔢 NUMBER-BASED RECURSION PROBLEMS (WITHOUT CODE)

# ### 1️⃣ Print Numbers from 1 to N

# Given a number **N**, print numbers from **1 to N** using recursion.

def pri(n):
    if n==0:
        return n
    pri(n-1)
    print(n) 
pri(3)
# ### 2️⃣ Print Numbers from N to 1

# Given a number **N**, print numbers from **N to 1** using recursion.

def pri(n):
    if n==0:
        return
    print(n)
    pri(n-1)
pri(3)

# ### 3️⃣ Find Sum of First N Natural Numbers

# Given **N**, find the sum of numbers from **1 to N** using recursion.

def sum(n):
    if n==0:
        return 5
    return n+sum(n-1)
print(sum(5))

# ### 4️⃣ Find Factorial of a Number

# Given a number **N**, find **N! (factorial)** using recursion.
def fact(n):
    if n==1:
        return n 
    return n*fact(n-1)
n=3
f=fact(n)
print(f'factorial of {n} is {f}')

# ### 5️⃣ Find Power of a Number

# Given two numbers **x** and **n**, compute **xⁿ** using recursion.

def pow(n,p):
    if p==0:
        return 1
    return n*pow(n,p-1)
a=pow(2,3)
print(f'power is {a}') 

# ### 6️⃣ Count Number of Digits in a Number

# Given an integer **N**, count how many digits it contains using recursion.

# def count(a):
#     if not a:
#         return 0
#     return 1+sumofdigit(a//10) 
# print(count(12345))    

# ### 7️⃣ Find Sum of Digits of a Number

# Given a number **N**, find the sum of its digits using recursion.

def sumofdigit(a):
    if not a:
        return 0
    return a%10+sumofdigit(a10) 
print(sumofdigit(12345))    

# ### 8️⃣ Reverse a Number

# Given a number **N**, reverse the digits using recursion.

# ---

# ### 9️⃣ Check Whether a Number Is Palindrome

# Given a number **N**, check whether it reads the same forward and backward using recursion.

# ---

# ### 🔟 Find GCD of Two Numbers

# Given two numbers **a** and **b**, find their **Greatest Common Divisor (GCD)** using recursion.

# ---

# ### 🎯 HOW TO PRACTICE THESE PROPERLY

# For **each problem**, do this:

# 1. Identify **base case**
# 2. Decide how to **reduce the number**
# 3. Trace 2–3 calls on paper
# 4. Then write code

# ---
