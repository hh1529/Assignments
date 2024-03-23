h=[1,2,3,4,5,6]
print("The original list : ",str(h))
g=[2,3,4]
if set(g).intersection(set(h)) == set(g):
    res = True
else:
    res = False

print("this is result : "+str(res))

