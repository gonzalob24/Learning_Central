import math

from Polygon import Polygon


class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def perimeter(self):
        a = (self.base / 2)
        c_sqred = a ** 2 + self.height ** 2

        return self.base + math.sqrt(c_sqred)


t1 = Triangle(5, 5)
print(t1.area())
