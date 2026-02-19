# Write a program that takes a string,
#  string should be of even length.
#  Divide the string into two equals parts,
#  check the number of vowels in both 
# the parts of the string. 
# If both parts of string have same number of vowels then return true otherwise return false.

# Testcase1	:  rebels
# Output     	:  true
# Explanation 	:  Given sring rebels divided into two parts, reb and els. In both parts vowels count is same that is 1(e is presented in both the parts) so it returns true.

# Testcase2	:  apples
# Output     	:  true

# Testcase1	:  mars
# Output     	:  false
def same(st):
    one=''
    sec=''
    av=0
    if len(st)%2==0:
        av=len(st)//2
    for i in range(len(st)):
        if i<av:
            if st[i] in 'aeiou':
                one+=st[i]
        else:
            if st[i] in 'aeiou':
                sec+=st[i]
    print(one,sec)
    if len(one)==len(sec):
        return True
    return False
print(same('rebeossi'))



