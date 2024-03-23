def newranges(n):
    if n in range(2,100):
        return("is in range")
    else:
        return("not in Range")
n=int(input("enter the no : " ))
print(newranges(n))