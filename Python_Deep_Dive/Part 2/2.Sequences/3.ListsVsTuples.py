## Creating Tuples ##
from dis import dis

dis(compile('(1, 2, 3, "a")', "string", "eval"))

dis(compile('[1, 2, 3, "a"]', "string", "eval"))

from timeit import timeit

print(timeit("tuple((1, 2, 3, 4, 5, 6, 7, 8, 9))", number=1_000_000))
print(timeit("list([1, 2, 3, 4, 5, 6, 7, 8, 9])", number=1_000_000))

def fn1():
    pass

dis(compile('(fn1, 10, 20)', "string", "eval"))
dis(compile('[fn1, 10, 20]', "string", "eval"))

dis(compile('([1, 2], 10, 20)', "string", "eval"))
dis(compile('[[1, 2], 10, 20]', "string", "eval"))

print(timeit("([1, 2], 10, 20)", number=1_000_000))
print(timeit("[[1, 2], 10, 20]", number=1_000_000))

## Copying Lists and Tuples
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(id(l1), id(t1))

l2 = list(l1)
t2 = tuple(t1)

print(timeit('tuple((1, 2, 3, 4, 5, 6, 7, 8, 9))', number=1_000_000))
print(timeit('list([1, 2, 3, 4, 5, 6, 7, 8, 9])', number=1_000_000))

# Let's look at the id's of the copies:
print(id(l1), id(l2), id(t1), id(t2))

print(l1 is l2, t1 is t2)

# Note that this is the case even if the tuple contains non constant elements:
t1 = ([1, 2], fn1, 3)
t2 = tuple(t1)
print(t1 is t2)

## Storage Efficiency ##
import sys

prev = 0
for i in range(10):
    c = tuple(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta: {delta}')

prev = 0
for i in range(10):
    c = list(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta: {delta}')

c = []
prev = sys.getsizeof(c)
print(f'0 items: {sys.getsizeof(c)}')
for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta: {delta}')

