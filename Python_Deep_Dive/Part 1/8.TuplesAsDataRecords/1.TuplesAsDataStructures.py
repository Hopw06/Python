a = ('a', 10, True)
b = 'b', 20, False
print(a)
print(b)

print(type(a))
print(type(b))

# unpacking
point = 10, 20, 30
x, y, z = point

print(x)
print(y)
print(z)

# tuple are imutable, but the elements inside can be mutable
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '{0}(x={1}, y={2})'.format(self.__class__.__name__, self.x, self.y)

a = Point2D(0, 0), Point2D(10, 10), Point2D(20, 20)
print(a)

a[0].x = 10
print(a)

# Tuples as Data Records
# instead of using Point2D class, we can use tuple as a Point
pt1 = (0, 0)
pt2 = (10, 10)

london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

cities = london, new_york, beijing

city_names = [t[0] for t in cities]
print(city_names)

print(sum(city[2] for city in cities))

# unpacking
city, country, population = new_york

print(city)
print(country)
print(population)

# we can also use extended unpacking:
record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, year, month, day, open_, high, low, close = record

print(symbol)
print(close)

symbol, year, month, day, *others, close = record
print(symbol, year, month, day, close)
print(others)

symbol, year, *_, close = record
print(symbol, year, close)
print(_)

for city, country, population in cities:
    print('city={0}, population={1}'.format(city, population))

for index, value in enumerate(beijing):
    print('{0}:{1}'.format(index, value))

# Another frequent application of usign tuples as data structures is for returning multiple values from a function.
from random import uniform
from math import sqrt

def random_shot(radius):

    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    return random_x, random_y, is_in_circle

num_attempts = 1_000_000
count_inside = 0

for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print("Pi is approximately: {0}".format(4 * count_inside / num_attempts))