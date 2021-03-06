# A callable is an object that can be called (using the () operator), and always returns a value
## Functions and Methods are callable ##
print(callable(print))

print(callable(len))

l = [1, 2, 3]
print(callable(l.append))

s = 'abc'
print(callable(s.upper))

## Callables always return a value ## 
# default is None

result = print("Hello")
print(result)

l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)

s = 'abc'
result = s.upper()
print(result)

## Classes are callable ##
from decimal import Decimal

print(callable(Decimal))

result = Decimal('10.5')
print(result)

## Class instances may be callable ##
class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0
    
    def __call__(self, x=1):
        self.counter += x
        print(self.counter)

my_obj = MyClass()

print(callable(my_obj.__init__))

print(callable(my_obj.__call__))

my_obj()

my_obj()

my_obj()