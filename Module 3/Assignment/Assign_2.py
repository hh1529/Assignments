def h(my_words):
    count=0
    for m in my_words:
        if len(m)>=2 and m[0]==m[-1]:
            count+=1
    return count
print(h(["harsh","rahul","him"]))