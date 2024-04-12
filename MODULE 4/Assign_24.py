# Write a Python class named Circle constructed by a radius and two 
# methods which will compute the area and the perimeter of a circle 

class Circle:
    def func(self,r):
        self.r=r
        print("Radius : ",r)
        
    def func2(self):
        print("area of Circle : ",3.14*self.r*self.r)

    def func3(self):
        print("Perimeter of Circle : ",2*3.14*self.r)

obj=Circle()
obj.func(10)
obj.func2()
obj.func3()