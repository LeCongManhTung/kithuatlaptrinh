print("le cong manh tung")
print("235752021610041")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Tạo một đối tượng hình tròn với bán kính là 5
circle = Circle(5)

# Tính và in ra diện tích của hình tròn
print("Diện tích hình tròn:", circle.area())

