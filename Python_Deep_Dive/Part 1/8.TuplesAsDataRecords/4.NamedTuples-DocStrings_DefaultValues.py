## Adding DocStrings to Named Tuples ##
# This is easy to do, both with generated class, as well as it's properties
from collections import namedtuple
Point2D = namedtuple('Point2D', ('x', 'y'))

Point2D.__doc__ = "Represents a 2D Cartesian coordinate"

Point2D.x.__doc__ = "x-coordinate"
Point2D.y.__doc__ = "y-coordinate"

# print(help(Point2D))

## Adding Default values to named tuples ##
# Using a prototype
Vector = namedtuple('Vector', 'x1 y1 x2 y2 origin_x origin_y')

vector_zeroorigin = Vector(x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)

v1 = vector_zeroorigin._replace(x1=1, y1=1, x2=10, y2=10)
print(v1)

# Using __defaults__
def func(a, b=20, c=30):
    print(a, b, c)

print(func.__defaults__)
func(10)

Vector.__new__.__defaults__ = (0, 0)
print(Vector.__new__.__defaults__)

v1 = Vector(0, 0, 10, 10, -10, -10)
print(v1)

v2 = Vector(5, 5, 20, 20)
print(v2)

v3 = Vector(x1=1, y1=1, x2=10, y2=10)
print(v3)

Vector.__new__.__defaults__ = (0,) * len(Vector._fields)
print(Vector())