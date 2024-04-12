# Write a Python program to read first n lines of a file.

n = int(input("enter The lines you read : "))
file = open("python.txt", "r")
for i in range(n):
    print(file.readline(), end="")
file.close()