# Integers are object - instead of the int class.
print(type(100))

# It will take up a variable amount of memory that depends on the particular size of the integer.

import sys

# Python 3.7
# Creating an integer object requires an overhead of 12 bytes.
print(sys.getsizeof(0))

# Here we see that to store the number 1 required 2 bytes (16 bits) on top of the 12 bytes overhead:
print(sys.getsizeof(1))

# Larger numbers will require more storage space:
print(sys.getsizeof(2**1000))

# Larger integer will also slow down calculations:
import time

def calc(a):
    for i in range(10000000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)


start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end - start)


start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)