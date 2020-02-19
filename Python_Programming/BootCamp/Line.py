import math


class Line:

    def __init__(self,coord1,coord2):
        """coord1 and coord2 are tuples of x, y coordinates"""
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        """returns the distance b/w two points"""
        x1, y1 = self.coord1
        x2, y2 = self.coord2

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def slope(self):
        """returns the slope of a line"""
        x1, y1 = self.coord1
        x2, y2 = self.coord2

        return ((y2 - y1) / (x2 - x1))


if __name__=="__main__":
    coord1 = (3, 2)
    coord2 = (8, 10)
    line1 = Line(coord1, coord2)
    print(line1.distance())
    print(line1.slope())
