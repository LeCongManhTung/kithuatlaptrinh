print("le cong manh tung")
print("235752021610041")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
     
        return math.pi * (self.radius ** 2)

    def circumference(self):
       
        return 2 * math.pi * self.radius
    
radius = float(input("Nhập bán kính của hình tròn: "))

circle = Circle(radius)

print("Diện tích hình tròn là:", circle.area())
print("Chu vi hình tròn là:", circle.circumference())

