from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.base + self.height)
    
    def calculate_area(self):
        return self.base * self.height

c = Circle(5)
s = Square(6)
r = Rectangle(6, 3)

print("Circle: ")
print(f"Perimeter: {c.calculate_perimeter()}")
print(f"Area: {c.calculate_area()}")

print("\nSquare: ")
print(f"Perimeter: {s.calculate_perimeter()}")
print(f"Area: {s.calculate_area()}")

print("\nSquare: ")
print(f"Perimeter: {r.calculate_perimeter()}")
print(f"Area: {r.calculate_area()}")