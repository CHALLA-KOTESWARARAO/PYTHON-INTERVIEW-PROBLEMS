lis=[10,20,30,40,50]
_1lar=0
_2lar=0
for i in lis:
    if i>_1lar:
        _1lar=i
for i in lis:
    if i<_1lar and i>_2lar:
        _2lar=i
print(_1lar)
print(_2lar)
