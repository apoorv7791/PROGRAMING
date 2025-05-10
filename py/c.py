import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def _gt_(self, other):
        return self.area() > other.area()


# example usage
c1 = Circle(5)
c2 = Circle(6)


if c2._gt_(c1):
    print("First Circle is greater")
else:
    print("Second is greater ")
