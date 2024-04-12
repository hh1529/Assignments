# Write a Python program to count the number of lines in a text file. 

file = open("python.txt","r")

count=0

for j in file:
    
    if j.split("."):
        count+=1

print(count)
file.close()