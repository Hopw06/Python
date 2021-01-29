## Named Tuples ##
# instead of
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
p1 = Point3D(2, 3, 4)

# use it
from collections import namedtuple

Point3D_ = namedtuple('Point3D', ('x', 'y', 'z')) # it just create a class Point3D which inherit from Point3D
p = Point3D_(2, 3, 4)
print(p)
print(p1)

print(isinstance(p, tuple))
print(isinstance(p1, tuple))

# by using namedtuple, we can use some functions: __repr__, __eq__

Point2D = namedtuple('Point2D', ('x', 'y'))

pt2d_1 = Point2D(10, 20)
pt2d_2 = Point2D(10, 20)

print(pt2d_1)
print(pt2d_2)
print(pt2d_1 == pt2d_2)

# Since it is a tuple, so we can use some functions

print(max(pt2d_1))
print(sum(e[0] * e[1] for e in zip(pt2d_1, pt2d_2)))

# Other Ways to specify field names

# There are a number of ways we can specify the field names for the named tuple:

# we can provide a sequence of strings containing each property name
# we can provide a single string with property names separated by whitespace or a comma

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])

circle_1 = Circle(0, 0, 10)
circle_2 = Circle(center_x = 10, center_y = 20, radius = 100)

print(circle_1)
print(circle_2)

City = namedtuple('City', 'name country population')
new_york = City('new_york', 'USA', 8_500_500)

print(new_york)

Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)

Stock = namedtuple('Stock', '''symbol
                                year month day
                                open high low close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)

## Accessing items in a Named Tuple
pt1 = Point2D(10, 20)
print(pt1.x)

print(circle_1.radius)

# Now named tuples are tuples, so elements can be accessed by index, unpacked, and iterated.

print(circle_1[2])

for item in djia:
    print(item)

x, y = pt1
print(x, y)

symbol, *_, close = djia
print(symbol, close)

# converst named tuples to dictionaries

d = djia._asdict()
print(d)