# Write a Python class named Rectangle constructed by a length and 
# width and a method which will compute the area of a rectangle

class rct:
    def func(self,l,b):
        self.l=l
        self.b=b
        print("length : ",l)
        print("braedth : ",b)
    def func2(self):
        print("area of Rectangle : ",self.l*self.b)

obj=rct()
obj.func(10,20)
obj.func2()