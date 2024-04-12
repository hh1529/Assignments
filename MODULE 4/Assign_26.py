# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python? 

k="inheritance Is Simply A heirarchy of class or Simply called realtion Between the Classes Or Simply The Concept of Heritance Ex you grandfather have propertt so it will give you to your father and after That it will given to you so this will also happens in the classes"
print(k)

class grandfather:
    def func(self):
        print(" More land")

class father(grandfather):
    def func2(self):
        print("More Money")
    
class Son(father,grandfather):
    def Func3(self):
        print("more Power")

obj=Son()
obj.func()
obj.func2()
obj.Func3()
print()

j="the Init is Simply A constructor Means It will execute When The Object is Created "
print(j)

l="The Constructor is Simply When there is a website started or at the start When The object Is Created it will started or executed "
print(l)