# Memory Footprint
import sys
from decimal import Decimal

a = 3.1415
b = Decimal("3.1415")

print(sys.getsizeof(a))
print(sys.getsizeof(b))
# Decimals take up a lot more memory than floats. 

# Computational Performance
# Decimal arithmetic is also much slower than floats arithmetic

import time
from decimal import Decimal

def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal("3.1415")

n = 10000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)

# add operators
def add_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def add_decimal(n=1):
    a = Decimal("3.1415")
    for i in range(n):
        a + a

start = time.perf_counter()
add_float(n)
end = time.perf_counter()
print('add_float: ', end - start)

start = time.perf_counter()
add_decimal(n)
end = time.perf_counter()
print('add_decimal: ', end - start)

# square root operator
import math
def sqrt_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def sqrt_decimal(n=1):
    a = Decimal("3.1415")
    for i in range(n):
        a.sqrt()

start = time.perf_counter()
sqrt_float(n)
end = time.perf_counter()
print('sqrt_float: ', end - start)

start = time.perf_counter()
sqrt_decimal(n)
end = time.perf_counter()
print('sqrt_decimal: ', end - start)