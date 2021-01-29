# Truncation
from math import trunc
print(trunc(10.3), trunc(10.5), trunc(10.6))

print(trunc(-10.3), trunc(-10.5), trunc(-10.6))

# The int contructor use trunc when a float is passed.

from math import floor, ceil

print(floor(10.3), floor(10.5), floor(10.6))

print(floor(-10.3), floor(-10.5), floor(-10.6))

print(ceil(10.3), ceil(10.5), ceil(10.6))

print(ceil(-10.3), ceil(-10.5), ceil(-10.6))