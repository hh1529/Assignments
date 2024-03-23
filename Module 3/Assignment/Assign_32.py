l=[1,2,3,4]
j=["java","python","html","c++"]
d={}
for k in l:
    for m in j:
        d[k]=m
        j.remove(m)
        break
print(d)