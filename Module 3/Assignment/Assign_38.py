str1 = 'w3resource'
my_dict = {}
for k in str1:
    my_dict[k] = my_dict.get(k,0) + 1
print(my_dict)