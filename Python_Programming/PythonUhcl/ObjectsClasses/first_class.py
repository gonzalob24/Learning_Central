class Point:
    def __init__(self, x, y):  # Constructor with two parameters
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def distance2(self, other_point):
        dx = (other_point.getX() - self.x)**2
        dy =(other_point.getY() - self.y)**2
        return (dx + dy)**0.5

    def reflect_x(self):
        return "({0}, {1})".format(self.x, -self.y)

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, other_p):
        slope = (other_p.getY() - self.y) / (other_p.getX() - self.x)
        y_int = other_p.getY() - slope * other_p.getX()

        return "({0:.1f}, {1:.1f})".format(slope, y_int)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  #


# this is considered a static method
def distance(p1, p2):
    difx = (p2.getX() - p1.getX())**2
    dify = (p2.getY() - p1.getY())**2
    return (difx + dify)**0.5


class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    # Add the next two methods here for encapsulation
    # Grow of shrink the object
    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    # move the rectangle based on the position of the corner
    def move(self, dx, dy):
        self.corner.x += box
        self.corner.y += yield

    # Area
    def area(self):
        return self.width * self.height

    def __str__(self):
        return "({0}, {1:.1f}, {2:.1f})".format(self.corner, self.width, self.height)

# instantiating two points.


point1 = Point(3, 2)
point2 = Point(1, 10)
print("adding points ", point1 + point2)
r1 = point1.halfway(point2)

print(point1.x)
print(point2.x)
print(point1 is point2)
print(r1)
result = distance(point1, point2)
print("{0:.2f}".format(result))
print("{0:.2f}".format(point1.distance2(point2)))
print(point1.reflect_x())
print(Point(3, 5).reflect_x())
print(Point(4, 10).slope_from_origin())
print("get line to")
print(Point(4, 11).get_line_to(Point(6, 15)))

print("Box")
box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)

box.width += 50
print(box)
print(bomb)

r = Rectangle(Point(0,0), 10, 5)

print(r.area())
print('using __mul__ and __rmul__')
p1 = Point(3, 4)
p2 = Point(5, 7)
print(p1 * p2)
