def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    
    return inner

def add(a, b = 0):
    """
    returns the sum of a and b
    """
    return a + b

print(help(add))

print(id(add))

add = counter(add) # the add function is decorated. counter is caled a decorator.

print(id(add))

print(add(1, 2))

print(add(2, 2))

# There are a shorthand way of decorating our function without having to type:
# func = counter(func)

@counter
def mult(a: float, b: float, c: float = 1) -> float:
    """
    returns the product of a, b and c.
    """
    return a * b * c

print(mult(1, 2, 3))

print(mult(2, 2, 2))

# Let's do a little bit of introspection on our two decorated functions:
print(add.__name__)
print(mult.__name__)

print(help(add))
print(help(mult))

# As you can see, we've also lost our docstring and parameter annotations!
import inspect

print(inspect.getsource(add))

print(inspect.getsource(mult))

print(inspect.signature(add))

print(inspect.signature(mult))

print(inspect.signature(add).parameters)

# In general, when we create decorated functions, we end up "losing" a lot of the metadata of our original function!
# However, we can put that information back in:
# by using wraps decorator
from functools import wraps

def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    
    return inner

@counter
def add(a: int, b: int=10) -> int:
    """
    return sum of two intergers
    """
    return a + b

print(help(add))

print(inspect.getsource(add))

print(inspect.signature(add).parameters)