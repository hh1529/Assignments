# Write a Python program to read a file line by line and store it into a list

file =open("python.txt","r")
h=[]
for j in file:
    h.append(j)

print(h)

file.close()