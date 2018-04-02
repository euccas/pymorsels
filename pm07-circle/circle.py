import math

class Circle():
    PI = 3.1415926

    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return "Circle({0})".format(self.radius)

    def __repr__(self):
        return "Circle({0})".format(self.radius)

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
