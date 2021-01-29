# A module is simply another data type. And the modules we use are instances of that data type.
import math

print(globals())

print(globals()['math'])

print(type(math))

print(id(math))

math = None

print(type(math))

print(id(math))

# re-import
import math

print(type(math))

print(id(math))

import sys

print(sys.modules)

print(sys.modules['math'])

print(id(sys.modules['math']))

print(math.__name__)
print(math.__dict__)

print(math.sqrt is math.__dict__['sqrt'])

# print(math.__file__)

# Now the math module is a little special - it is written in C and actually a built-in.

# Let's look at another module from the standard library:

import fractions

print(fractions.__dict__)
print(fractions.__file__)

# create dynamically module
import types

print(isinstance(fractions, types.ModuleType))

# print(help(types.ModuleType))

mod = types.ModuleType('point', 'A module for handling points.')
print(mod)
print(help(mod))

# OK, so now let's add some functionality to it by simply setting some attributes:
from collections import namedtuple
mod.Point = namedtuple('Point', ('x', 'y'))

def points_distance(pt1, pt2):
    return math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y) ** 2)

mod.distance = points_distance

print(mod.__dict__)

p1 = mod.Point(0, 0)
p2 = mod.Point(1, 1)

print(mod.distance(p1, p2))