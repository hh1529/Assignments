file=open("python.txt","a")
file.write(" \n python is very useful language")
file.close()

file=open("python.txt","r")
print(file.readline())
print(file.readline())
file.close()