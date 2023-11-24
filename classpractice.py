import math
class area:
    def __init__(self,length,breadth,radius): #SELF MEANS AREA  AREA'S INTINSE
        self.l = length
        self.b = breadth
        self.r = radius
    def circle(self):
        area = math.pi*self.r*self.r
        print("Area of circle is",area)
    def rectangle(self):
        area = self.l*self.b
        print("Area of rectangle is",area)
#a1 = area(10,20,5)
#a1.circle()      
#a1.rectangle()  