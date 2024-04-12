# Write a Python program to read a file line by line store it into a variable.

file =open("python.txt","r")
h=""
for j in file:
    h+=j

print(h)

file.close()
