class Point:
    def __init__ (self,a=0,b=0):
        self.a = a 
        self.b = b
    def __str__(self):
        return "({0} , {1})" . format(self.a ,self.b)
p1 = Point(8,9)
print(p1)