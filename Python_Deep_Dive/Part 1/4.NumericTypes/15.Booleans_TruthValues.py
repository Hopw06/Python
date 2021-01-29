# All objects in Python have an associated truth value, or truthyness
# All objects implement a __bool__ function

a = 1
print(bool(a)) # a.__bool__()

# or
if a: # a.__bool__()
    print(True)

# Numeric Types:
from fractions import Fraction
from decimal import Decimal
print(bool(10), bool(1.5), bool(Fraction(3, 4)), bool(Decimal('10.5')), bool(1j))

print(bool(0), bool(0.0), bool(Fraction(0, 1)), bool(Decimal('0')), bool(0j))

# Sequence Types
print(bool([1, 2, 3]), bool((1, 2, 3)), bool('abc'))

print(bool([]), bool(()), bool(''))

# Mapping Types
print(bool({'a': 1}), bool({1, 2, 3}))

print(bool({}), bool(set()))

# None Types
print(bool(None))

# One application of truth values
a = [1, 2, 3]
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = []
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = 'abc'
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = ''
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

# We could write like this:
a = 'abc'
if a is not None and len(a) > 0:
    print(a)

# BUT
a = ''
if a is not None:
    print(a[0]) # error
    
a = None
if len(a) > 0:
    print(a[0]) # error