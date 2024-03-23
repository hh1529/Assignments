h=int(input("enter The Range : "))
x=0
y=1
z=y
count=1
while (count<=h):
      print(z,end=" ")
      count+=1
      x,y=y,z
      z=x+y
print()