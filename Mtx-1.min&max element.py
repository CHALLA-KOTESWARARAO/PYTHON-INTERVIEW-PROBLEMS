a=[
    [5,4,9],
    [8,7,6],
    [1,2,3]
]
min=float('inf')
max=float('-inf')
for i in a:
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print("min:",min)
print("max:",max)
