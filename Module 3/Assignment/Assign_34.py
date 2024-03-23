h={
    "harsh":1,
    "aibs":2,
    "ha" :1,
    "ja":2,
    "ka":3
}
z=h.values()
j=[]
for i in z:
    if i not in j:
        j.append(i)
print(j)