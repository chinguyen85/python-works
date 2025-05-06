# S principle: Single Responsibility Principle
# A class should have only one reason to change, meaning that a class should have
# only one job.

class Shape:
    def rectangle(self, width, height):
        print(f"Rectangle demensions: {width} and {height}")

    def square(self, length):
        print(f"Square demensions: {length} and {length}")

###############################################################################
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Dimensions of Rectangle: {self.width} and {self.height}")
              
class Square:
    def __init__(self, length):
        self.length = length

    def draw(self):
        print(f"Dimensions of Square: {self.length}")