# Example 1
# generic

def audit(f):
    def inner(*args, **kwargs):
        print(f'Called {f.__name__}')
        return f(*args, **kwargs)
    return inner

@audit
def say_hello(name):
    return f'Hello {name}'

from operator import mul
from functools import reduce

@audit
def product(*values):
    return reduce(mul, values)

say_hello('Polly')
print(product(1, 2, 3, 4))

# example 2
# same thing here - using *item_values makes more sense than *args:
def count_multi(lst, *item_values):
    return sum(lst.count(value) for value in item_values)

l = 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10

print(count_multi(l, 1, 6, 7))

# example 3
# Suppose we want our class init to allow people to send in additional arbitrary (custom) instance attributes:

class Person:
    def __init__(self, name, age, **custom_attrs):
        self.name = name
        self.age = age
        for attr_name, attr_value in custom_attrs.items():
            setattr(self, attr_name, attr_value)

parrot = Person('Polly', 101, status='stiff', vooms=False)

print(vars(parrot))

michael = Person('Michael', 42, role = 'shopkeeper', crooked = True)

print(vars(michael))