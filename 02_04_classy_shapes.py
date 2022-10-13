# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle():

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        self.area = self.length * self.breadth
        print(f"the area of the rectangle is {self.area}")

    def colour(self):
        print("the colour of the rectangle is blue")

class Circle():

    def __init__(self, radius):
        self.radius = radius 

    def circumfrence(self):
        self.circumfrence = 2 * self.radius * 3.147 
        print(f"the circumfrence of the circle is {self.circumfrence}")

rec = Rectangle(4, 6)
cerc = Circle(6)

rec.area()
rec.colour()
cerc.circumfrence()