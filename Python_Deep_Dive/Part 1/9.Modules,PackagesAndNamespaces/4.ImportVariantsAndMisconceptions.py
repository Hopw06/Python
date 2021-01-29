import sys
for key in sorted(sys.modules.keys()):
    print(key)

print('cmath' in sys.modules)

from cmath import exp

print('cmath' in globals())

print('exp' in globals())

# but cmath is already loaded in sys.modules
print(sys.modules['cmath'])

cmath = sys.modules['cmath']

print(cmath)

print(exp(2 + 3j))

print(cmath.sqrt(1 + 1j))

# we can:
import math as r_math
import cmath as c_math

print(r_math)
print(c_math)

print(r_math.sqrt(2))
print(c_math.sqrt(2))

# By the way, this is the exact same result as doing:
import importlib

r_math = importlib.import_module('math')
c_math = importlib.import_module('cmath')

print(r_math)
print(c_math)