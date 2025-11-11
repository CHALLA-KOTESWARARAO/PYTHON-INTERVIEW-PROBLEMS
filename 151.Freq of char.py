a='i love python'
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

#version 2
for char in a:
    dic[char] = dic.get(char, 0) + 1
print(dic)

