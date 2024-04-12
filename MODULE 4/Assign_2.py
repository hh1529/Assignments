    # Write a Python program to read an entire text file

file=open("python.txt","w")
file.write("Python is very easy to use")
file.write("\n")
file.close()

file=open("python.txt","r")
print(file.readlines())
file.close()