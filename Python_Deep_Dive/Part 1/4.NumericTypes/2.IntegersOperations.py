print(type(2 + 3))

print(type(3 -10))

print(type(3 * 5))

print(type(3 ** 4))

# But / always in a float value
print(type(2 / 3))

print(type(10 / 2))

# The math.floor() method will return the floor value of any number.

import math

# positive number
print(math.floor(3.15))

print(math.floor(3.99999))

# But negative number:
print(math.floor(-3.15))

print(math.floor(-3.99999))

# The floor division operator
# a // b = math.floor(a / b)
a = -33
b = 16
print('{0} / {1} = {2}'.format(a, b, a / b))
print('trunc({0} / {1}) = {2}'.format(a, b, math.trunc(a / b)))
print('{0} / {1} = {2}'.format(a, b, a // b))
print('floor({0} / {1}) = {2}'.format(a, b, math.floor(a / b)))

# The Modulo Operator %
# a = b * (a // b) + (a % b)

a = 13
b = 4

print('{0} / {1} = {2}'.format(a, b, a / b))
print('{0} / {1} = {2}'.format(a, b, a // b))
print('{0} / {1} = {2}'.format(a, b, a % b))
print(a == b * (a // b) + a % b)

a = -13
b = 4

print('{0} / {1} = {2}'.format(a, b, a / b))
print('{0} / {1} = {2}'.format(a, b, a // b))
print('{0} / {1} = {2}'.format(a, b, a % b))
print(a == b * (a // b) + a % b)

a = -13
b = -4

print('{0} / {1} = {2}'.format(a, b, a / b))
print('{0} / {1} = {2}'.format(a, b, a // b))
print('{0} / {1} = {2}'.format(a, b, a % b))
print(a == b * (a // b) + a % b)