## DIV and MOD ##
# div and mod with integer and decimal are same in case of positive number.
import decimal
from decimal import Decimal

x = 10
y = 3
print(x // y, x % y)
print(divmod(x, y))
print(x == y * (x // y) + x % y)

a = Decimal('10')
b = Decimal('3')
print(a // b, a % b)
print(divmod(a, b))
print(a == b * (a // b) + a % b)

# But negative numbers:

x = -10
y = 3
print(x // y, x % y)
print(divmod(x, y))
print(x == y * (x // y) + x % y)

a = Decimal('-10')
b = Decimal('3')
print(a // b, a % b)
print(divmod(a, b))
print(a == b * (a // b) + a % b) # But both of it still satisfy the equation:  n = d * (n // d) + (n % d)

## Other Mathematical Functions ##
# The Decimal class implements a variety of mathematical functions
a = Decimal('1.5')
print(a.log10())
print(a.ln())
print(a.exp())
print(a.sqrt())

# Although you can use the math function of the math module, be aware that the math module will cast Decimal numbers to floats when it performs the various operations.
import math
x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

x = 0.01
x_dec = Decimal('0.01')

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)