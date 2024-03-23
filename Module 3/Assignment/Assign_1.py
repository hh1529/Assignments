h=[]
j=int(input("enter the numbers in list : "))
for k in range(j):
    l=int(input("enter the number : "))
    h.append(l)
    b=sum(h)
print("sum ",b)
print("max number : ",max(h))
print("min number : ",min(h))