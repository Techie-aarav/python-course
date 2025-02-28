class square:
    def __init__(self,side):
        self.side = side
    def area(self):
        print("Area of square is:" , self.side**2)
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Area of circle is:" , 3.14*self.radius*self.radius)
asquare = square(16)
acircle = circle(10)
for shape in (asquare,acircle):
    shape.area()

