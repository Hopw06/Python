# Maximum and Minimum
l = [5, 8, 6, 10, 9]

# max
_max = lambda a, b: a if a > b else b

def max_seq(seq):
    rs = seq[0]
    for i in seq:
        rs = _max(i, rs)
    return rs

print(max_seq(l))

# min
_min = lambda a, b: a if a < b else b

def min_seq(seq):
    rs = seq[0]
    for i in seq:
        rs = _min(i, rs)
    return rs

print(min_seq(l))

# or better by passing function

def reduce(fn, seq):
    rs = seq[0]
    for i in seq[1:]:
        rs = fn(i, rs)
    return rs

print(reduce(_max, l))
print(reduce(_min, l))

# or just using lambda
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))

# Using same approach we can add all elements of a sequence together:
print(l)

print(reduce(lambda a, b: a + b, l))

# Python actually implements a reduce function, which is found in the functools module. Unlike our _reduce function, it can handle any iterable, not just sequences.
from functools import reduce

print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a + b, l))

# We have built-in function max(), min(), and sum() to calculate value:
print(max(l))

print(min(l))

print(sum(l))

## The any and all built-ins:
# Python provides two additional built-in reducing functions: any and all.

# The any function will return True if any element in the iterable is truthy:

# any: True if all elements are falsey
l = [0, 1, 2]

print(any(l))

l = [0, 0, 0]

print(any(l))

# all: True if all elements are truthy:
l = [0, 1, 2]
print(all(l))

l = [1, 2, 3]
print(all(l))

# We can use reduce to implement all and any.
# any
l = [0, 1, 2]
print(reduce(lambda x, y: bool(x or y), l))

l = [0, 0, 0]
print(reduce(lambda x, y: bool(x or y), l))

# all
l = [0, 1, 2]
print(reduce(lambda x, y: bool(x and y), l))

l = [1, 2, 3]
print(reduce(lambda x, y: bool(x and y), l))

# Calculate products
def mult(a, b):
    return a * b

l = [2, 3, 4]
print(reduce(mult, l))

print(reduce(lambda x, y: x * y, l))

# Calculate factorials
n = 5
print(reduce(lambda a, b: a * b, range(1, n + 1)))

## reduce initializer ##
# We can set default return value for reduce function.
l = [1, 2, 3]
print(reduce(lambda a, b: a * b, l))

# but 
l = []
# print(reduce(lambda a, b: a * b, l)) # error

# set defaul return value = 1
print(reduce(lambda a, b: a * b, l, 1))