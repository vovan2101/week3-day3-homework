import math

class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
obj = circle(7)
print("Площадь круга:", round(obj.area(), 2))