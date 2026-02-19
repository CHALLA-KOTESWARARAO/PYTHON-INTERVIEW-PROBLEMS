### 7️⃣ Longest Substring Without Repeating Characters

# **Problem:**
# Find the length of the longest substring with all unique characters.

def su(s):
    seen=set()
    l=0
    long=0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l+=1
        seen.add(s[r])
        long=max(long,r-l+1)
    return long
print(su("abcabcab"))