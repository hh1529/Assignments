# Write a Python program to read last n lines of a file

n = int(input(" enter the no of line from last :  "))
file = open("python.txt", "r")
lines = file.readlines()
for line in lines[-n:]:
    print(line, end="")
file.close()