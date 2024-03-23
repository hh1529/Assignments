list1 = [1, 3, 4, 55]
list2 = [90, 22,]
count = 0
for j in list2:
    if j in list1:
        count = 1
if count == 1:
    print("True") 
else :
    print("False")