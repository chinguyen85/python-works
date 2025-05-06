# Open/Closed Principle: A class should be open for extension,
# but closed for modification.

class Shape:
    def rectangle (self, width, height):
        print(f"Rectangle dimensions: {width} and {height}")

    def square(self, length):
        print(f"Square dimensions: {length} and {length}")
    
    def triangle(self, a, b, c):
        print(f"Triangle dimensions: {a}, {b} and {c}")

    def circle(self, radius):
        print(f"Circle dimensions: {radius}")

###############################################################################

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Dimensions of Rectangle: {self.width} and {self.height}")

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def draw(self):
        print(f"Dimensions of Square: {self.length}")

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"Dimensions of Triangle: {self.a}, {self.b} and {self.c}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Dimensions of Circle: {self.radius}")