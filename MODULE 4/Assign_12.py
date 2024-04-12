# Write a Python program to copy the contents of a file to another file. 

file=open("harsh.txt","r")
k=""
for j in file:
    k+=j
print(k)
file.close()

file=open("python.txt","a")
file.write("\n")
file.write(k)
file.close()

file=open("python.txt","r")
print(file.readlines())
