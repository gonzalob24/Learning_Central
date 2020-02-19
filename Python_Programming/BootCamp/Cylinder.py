import math


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * math.pow(self.radius, 2) * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.radius + self.height)


if __name__ == "__main__":
    c1 = Cylinder(2, 3)
    print(c1.volume())
    print(c1.surface_area())
