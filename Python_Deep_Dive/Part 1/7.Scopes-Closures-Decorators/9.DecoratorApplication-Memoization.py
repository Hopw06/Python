def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

# memoization using decorator.
from functools import wraps

def memoize(fn):
    cache = {1: 1, 2: 2}

    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print(fib(10))
# Make code more generic

def memoize(fn):
    cache = {1: 1, 2: 1}

    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    
    return inner

@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print(fib(10))

print(fib(20))

@memoize
def fact(n):
    print('Calculating fact({0})'.format(n))
    return 1 if n < 2 else n * fact(n - 1)

print(fact(10))

print(fact(20))

from functools import lru_cache

@lru_cache()
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print(fib(10))

print(fib(20))

@lru_cache()
def fact(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 2 else n * fact(n - 1)

print(fact(10))

print(fact(20))


# lru_cache with arguments
# [LRU Cache = Least Recently Used caching: since the cache is not unlimited, at some point cached entries need to be discarded, and the least recently used entries are discarded first]

@lru_cache(maxsize=8)
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print(fib(10))
print(fib(20))
print(fib(10)) # it has to recalculate.