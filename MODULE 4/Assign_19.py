# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets. 

k="Now Firstly Try Execute then it will go to Except And it will Throw The Message which is there in except and also Finally Will also gets Executed Because It will always Execute often There is a error or not"
print(k)

try:
    v="there Is an easy solution"
    print(v)
except:
    print(NameError,ValueError,KeyError)
finally:
    print("This is Exceptional handling")
