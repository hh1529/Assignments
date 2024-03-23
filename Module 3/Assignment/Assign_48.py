def fun(n):
    f = [1]
    for i in range(2,n):
        if n % i==0:
            f.append(i)
    return sum(f)
print(fun(5))
print(fun(10))            
