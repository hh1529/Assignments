#  Write a python program to find the longest words. 

file = open("python.txt", "r")
j=""
for m in file:
    j+=m
    
    
words = j.split()


longest_words = []
max_length = 0

for word in words:
    word = word.strip()
    word_length = len(word)

    if word_length > max_length:
        longest_words = [word]
        max_length = word_length

print(longest_words)
file.close()