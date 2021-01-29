# There are two constructors in int class. 
# int(x = 0) -> integer
# int(x, base = 10) -> integer
# Convert a number or string to an integer, or return 0 if no argument ar given. 
print(int(10))

print(int(10.9))

print(int(-10.9))

from fractions import Fraction

a = Fraction(22, 7)

print(a)

print(int(a))

print(int("10"))

print(int("101", base = 2))

# Python uses a-z for base from 11 to 36.
# Note that the letters are not case sensitive.

print(int("F1A", base = 16))

print(int("f1a", base = 16))

# Of course, the string must be a valid number in whatever base you specify.

#print(int("B1A", base = 11)) # Error

print(int("B1A", base = 12))

## BASE REPRESENTATIONS ##

print(bin(10))

print(oct(10))

print(hex(10))

a = int('1010', 2)

b = int('0b1010', 2)

c = 0b1010

print(a, b, c)

a = int('f1a', 16)
b = int('0xf1a', 16)
c = 0xf1a

print(a, b, c)

# not case-sensitive
a = 0xf1a
b = 0xf1a
c = 0xF1A

print(a, b, c)

## Custom Rebasing ##
# Python only provides built-in function to rebase to base 2, 8, 16
# For other base:

def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    if n < 0:
        raise ValueError("Number n must be >= 0")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n = n // b
    
    return digits

print(from_base10(10, 2))

print(from_base10(255, 16))

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")

    return ''.join([digit_map[d] for d in digits])

print(encode([1, 0, 1], "FT"))

print(encode([1, 10, 11], "0123456789AB"))

# Combine two above function

def rebase(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")

    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


print(rebase(131, 11))

print(rebase(4096, 16))

print(rebase(-4095, 16))
