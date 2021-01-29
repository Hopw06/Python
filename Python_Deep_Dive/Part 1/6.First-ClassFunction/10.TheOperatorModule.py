# A variety of arithmetic operators are implemented
import operator

print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.pow(2, 3))
print(operator.mod(13, 2))
print(operator.floordiv(13, 2))
print(operator.truediv(1, 3))

# These would have been very handy in our previous section:
from functools import reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4])) 
# or
print(reduce(operator.mul, [1, 2, 3, 4]))

## Comparison and Boolean Operations ##
print(operator.lt(10, 100))
print(operator.le(10, 10))
print(operator.is_('abc', 'def'))

# We can even get the truthyness of an object:
print(operator.truth([1, 2]))

print(operator.truth([]))

print(operator.and_(True, False))

print(operator.or_(True, False))

## Element and Attribute Getters and Setters ##

my_list = [1, 2, 3, 4]
print(my_list[1])

# Or
print(operator.getitem(my_list, 1))

my_list = [1, 2, 3, 4]
my_list[1] = 100
del my_list[3]
print(my_list)

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
operator.delitem(my_list, 3)
print(my_list)

# We can also do the same thing using the operator module's itemgetter function.

# The difference is that this returns a callable:
my_list = [1, 2, 3, 4]
f = operator.itemgetter(2)

print(f(my_list))

x = 'python'
print(f(x))

f = operator.itemgetter(2, 3)

print(f(my_list))
print(f(x))


# Similarly, operator.attrgetter does the same thing, but with object attributes.
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    
    def test(self):
        print("test method running...")

obj = MyClass()
print(obj.a, obj.b, obj.c)

f = operator.attrgetter('a')
print(f(obj))

my_var = 'b'
print(operator.attrgetter(my_var)(obj))

my_var = 'c'
print(operator.attrgetter(my_var)(obj))

f = operator.attrgetter('a', 'b', 'c')
print(f(obj))


# Of course, attributes can also be methods.

# In this case, attrgetter will return the object's test method - a callable that can then be called using ():

operator.attrgetter('test')(obj)()


# Of course, we can achieve the same thing using functions or lambdas:

f = lambda x: (x.a, x.b, x.c)
print(f(obj))


f = lambda x: (x[2], x[3])
print(f([1, 2, 3, 4]))
print(f('python'))

## Use Case ##
# Sorting
a = 2 + 5j
print(a.real)

l = [10 + 1j, 8 + 2j, 5 + 3j]
print(sorted(l, key = operator.attrgetter('real')))

l = ['aaz', 'aad', 'aaa', 'aac']
print(sorted(l, key = operator.itemgetter(-1)))
print(sorted(l, key = lambda x: x[-1]))

l = [(2, 3, 4), (1, 2, 3), (4, ), (3, 4)]
print(sorted(l, key = operator.itemgetter(0)))
print(sorted(l, key = lambda x: x[0]))

# Slicing
l = [1, 2, 3, 4]
print(l[0:2])
l[0:2] = ['a', 'b', 'c']
print(l)

del l[3:5]
print(l)

# We can do the same thing this way:
l = [1, 2, 3, 4]

print(operator.getitem(l, slice(0, 2)))
operator.setitem(l, slice(0, 2), ['a', 'b', 'c'])
print(l)

operator.delitem(l, slice(3, 5))
print(l)

# Calling another callable:
x = 'python'
print(x.upper())

print(operator.methodcaller('upper')('python'))

x = 'python'
print(operator.attrgetter('upper')(x)())

# If the callable takes in more than one parameter, they can be specified as additional arguments in methodcaller:
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, c):
        print(self.a, self.b, c)
    
obj = MyClass()
obj.do_something(30)

operator.methodcaller('do_something', 100)(obj)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, *, c):
        print(self.a, self.b, c)

obj = MyClass()

operator.methodcaller('do_something', c = 99)(obj)