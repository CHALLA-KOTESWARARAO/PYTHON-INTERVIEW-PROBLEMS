s="python"
rev=''
for i in s:
    rev=i+rev
print(rev)
revv="ko"
print(revv[:-1])
def rev(s):
    if s=='':
        return s
    else:
        return s[-1]+rev(s[:-1])
print(rev("koti"))
