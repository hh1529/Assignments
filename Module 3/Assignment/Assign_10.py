list=[1,5,8,7,46,45]
h=list[0]
j=list[1]
for i in range(2,len(list)):
    if list[i] < h:
        j=h
        h=list[i]
    elif list[i] < h:
        j=list[i]
    
print(j)
print(h)
