# Float class has a single constructor, which can take a number or a string an will attempt to convert it to a float.

print(float(10))

print(float(3.14))

print(float('0.1'))

# print(float('22/7')) # error

# SHOULD
from fractions import Fraction
frac = Fraction('22/7')

print(float(frac))

# Float do not always have an exact representation:
print(0.1)

print(format(0.1, '.25f'))

print(format(0.125, '.25f'))