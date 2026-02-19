## 🪟 Sliding Window Technique — Basics Made Easy

The **sliding window** is a problem-solving technique used mainly with **arrays** and **strings** to efficiently process **subarrays / substrings**.

Instead of checking every possible subarray (slow), we **reuse previous work** by sliding a “window” over the data.

---

## 🔹 What is a Sliding Window?

Imagine a **window** that covers part of an array/string.

* The window has a **start** and **end**
* We **move (slide)** the window step by step
* While sliding, we **update the result** instead of recalculating from scratch

### Simple visualization

```
Array:   [1, 2, 3, 4, 5]
Window:   [1, 2, 3]
Slide →      [2, 3, 4]
Slide →         [3, 4, 5]
```

---

## 🔹 Why Sliding Window?

| Without Sliding Window | With Sliding Window   |
| ---------------------- | --------------------- |
| O(n²) (slow)           | O(n) (fast)           |
| Recalculate again      | Reuse previous result |

---

## 🔹 Types of Sliding Window

### 1️⃣ Fixed Size Sliding Window

Window size is **constant**

**Examples:**

* Maximum sum of `k` elements
* Average of `k` numbers
* Subarray of size `k`

#### How it works

1. Create first window
2. Slide window by:

   * Removing left element
   * Adding next element

---

### 🟢 Basic Example (Fixed Size)

**Problem:**
Find **maximum sum of subarray of size 3**

**Input:**

```

```

**Windows & sums**

```
[2, 1, 5] → sum = 8
[1, 5, 1] → sum = 7
[5, 1, 3] → sum = 9  ✅
[1, 3, 2] → sum = 6
```

**Answer:** `9`

🧠 Instead of adding all elements again, we:

* subtract `2`
* add `3`

---

### 2️⃣ Variable Size Sliding Window

Window size **changes dynamically**

Used when:

* Condition is involved
* Size is NOT given

**Examples:**

* Longest substring without repeating characters
* Smallest subarray with sum ≥ X
* Longest subarray with sum ≤ K

---

### 🟢 Basic Example (Variable Size)

**Problem:**
Find **longest subarray with sum ≤ 5**

**Input:**

```
Array = [1, 2, 1, 1, 1, 3]
```

**Idea**

* Expand window by moving `end`
* If sum > 5 → shrink window from `start`

**Steps**

```
[1,2,1,1] → sum = 5 (valid)
[1,2,1,1,1] → sum = 6 ❌ → shrink
```

**Answer:** Length = `4`

---

## 🔹 Sliding Window in Strings

Common string problems:

* Longest unique substring
* Anagram check
* Pattern matching

### 🟢 Simplest String Example

**Problem:**
Find **length of longest substring without repeating characters**

**Input:**

```
"abcabcbb"
```

**Windows**

```
"abc" → length = 3
"bca" → length = 3
"cab" → length = 3
```

**Answer:** `3`

(Window grows → repeat found → shrink)

---

## 🔹 When to Use Sliding Window?

Ask yourself:
✔ Is it **array or string**?
✔ Is it **subarray / substring**?
✔ Do I need **maximum / minimum / longest / shortest**?

If yes → **Sliding Window** 🪟

---

## 🔹 One-Line Memory Trick 🧠

* **Fixed size** → size given (`k`)
* **Variable size** → condition given (sum, unique, limit)

---

## 🔹 Simplest Practice Question for You

👉 **Find maximum sum of subarray of size 2**

**Input:**

```
[1, 4, 2, 10, 2]
```

Great 👍
I’ll give you **practice problems from very easy → easy → medium**, all **sliding window only**, **NO code**, just **problem statements + input/output** so you can try yourself.

---

## 🟢 LEVEL 1 – Very Easy (Fixed Size Window)

### 1️⃣ Maximum Sum of Subarray (size = 2)

**Problem:**
Find the maximum sum of any subarray of size `2`.

**Input:**

```
Array = [1, 4, 2, 10, 2]
k = 2
```

**Expected Output:**

```
12
```

---

### 2️⃣ Average of Subarray (size = 3)

**Problem:**
Find the **maximum average** of any subarray of size `3`.

**Input:**

```
Array = [2, 1, 5, 1, 3, 2]
k = 3
```

**Expected Output:**

```
3
```

---

### 3️⃣ Maximum Sum of Subarray (size = 4)

**Problem:**
Find the maximum sum of a subarray of size `4`.

**Input:**

```
Array = [1, 2, 3, 4, 5, 6]
k = 4
```

**Expected Output:**

```
18
```

---

## 🟡 LEVEL 2 – Easy (Variable Size Window)

### 4️⃣ Smallest Subarray with Sum ≥ 7

**Problem:**
Find the **length of the smallest subarray** whose sum is **≥ 7**.

**Input:**

```
Array = [2, 1, 5, 2, 3, 2]
```

**Expected Output:**

```
2
```

---

### 5️⃣ Longest Subarray with Sum ≤ 5

**Problem:**
Find the **length of the longest subarray** with sum **≤ 5**.

**Input:**

```
Array = [1, 2, 1, 1, 1, 3]
```

**Expected Output:**

```
4
```

---

### 6️⃣ Longest Subarray of 1’s (k = 1 flip allowed)

**Problem:**
You can flip at most **1 zero to 1**.
Find the **longest subarray of 1’s**.

**Input:**

```
Array = [1, 1, 0, 1, 1, 0, 1]
k = 1
```

**Expected Output:**

```
5
```

---

## 🔵 LEVEL 3 – Strings (Sliding Window)

### 7️⃣ Longest Substring Without Repeating Characters

**Problem:**
Find the length of the longest substring with all unique characters.

**Input:**

```
"abcabcbb"
```

**Expected Output:**

```
3
```

---

### 8️⃣ Longest Substring with At Most 2 Distinct Characters

**Problem:**
Find the length of the longest substring containing **at most 2 distinct characters**.

**Input:**

```
"eceba"
```

**Expected Output:**

```
3
```

---

### 9️⃣ Count of Substrings of Size 3 with Unique Characters

**Problem:**
Count how many substrings of size `3` have all unique characters.

**Input:**

```
"xyzzaz"
```

**Expected Output:**

```
1
```

---

## 🔴 LEVEL 4 – Slightly Challenging

### 🔟 Longest Subarray with Exactly K Odd Numbers

**Problem:**
Find the length of the longest subarray containing **exactly 2 odd numbers**.

**Input:**

```
Array = [2, 2, 1, 2, 1, 2, 2]
k = 2
```

**Expected Output:**

```
5
```

---

## 🧠 How You Should Solve (Important)

For **each problem**, do this on paper:

1. Draw array/string
2. Mark `start` and `end`
3. Slide window step-by-step
4. Track sum / count / map
5. Update answer

---

### 🔥 Next Step?

Reply with:

* **Problem number you solved**, and
* **Your steps (not code)**

I’ll **correct your logic** and then give you **simple code** once you’re confident 💪
