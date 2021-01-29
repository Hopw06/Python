# Rational Numbers
from fractions import Fraction

print(Fraction(1))

print(Fraction(1, 3))

# Using rational numbers
x = Fraction(2, 3)
y = Fraction(3, 4)

print(Fraction(x, y))

# Float

print(Fraction(0.125))

print(Fraction(0.5))

# String
print(Fraction('10.5'))

print(Fraction('22/7'))

# fractions are automatically reduced:

print(Fraction(8, 16))

print(Fraction(1, -4))

# OPERATORS
print(Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3))

print(Fraction(1, 2) * Fraction(1, 4))

print(Fraction(1, 2) / Fraction(1, 3))

# We can recover the numerator and denominator (integers):
x = Fraction(22, 7)
print(x.numerator)
print(x.denominator)

# since floats have finite precision, any float can be converted to a rational number:
import math
x = Fraction(math.pi)
print(x)
print(float(x))

x = Fraction(math.sqrt(2))
print(x)

## Beware! ##
# Float number representations (as we will examine in future lessons) do not always have an exact representation

print(Fraction(3, 10))
# different
print(Fraction(0.3))

# Because python try to round value to better display format:
x = 0.3

print(format(x, '.5f'))

print(format(x, '.15f'))

print(format(x, '.25f'))

# Constraining the denominator
x = Fraction(math.pi)
print(x)
print(format(float(x), '.25f'))

y = x.limit_denominator(10)
print(y)
print(format(float(y), '.25f'))

y = x.limit_denominator(100)
print(y)
print(format(float(y), '.25f'))

y = x.limit_denominator(500)
print(y)
print(format(float(y), '.25f'))