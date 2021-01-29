# define
a = complex(1, 2)
b = 1 + 2j

print(a)
print(b)
print(a == b)

print(a.real, type(a.real))
print(b.real, type(b.real))

# operator
a = 1 + 2j
b = 3 - 4j
c = 5j
d = 10

print(a + b)
print(b * c)
print(c / d)
print(d - a)

# but // and % are not defined for complex numbers.

# == and !=, same problem with like float
a = 0.1j
print(a + a + a == 0.3j)

# math functions: the cmath module provides complex alternatives to the standard math functions
import math
import cmath

a = 1 + 5j
print(cmath.sqrt(a))
# Polar / Rectangular conversions
a = 1 + 1j
r = abs(a) # return magnitude of the complex number
phi = cmath.phase(a)

print('{0} = ({1}, {2})'.format(a, r, phi))

r = math.sqrt(2)
phi = cmath.pi / 4
print(cmath.rect(r, phi))

# Euler's Identity and the isclose() function
RHS = cmath.exp(cmath.pi * 1j) + 1
print(RHS)

print(cmath.isclose(RHS, 0, abs_tol=0.00001))
print(cmath.isclose(RHS, 0))