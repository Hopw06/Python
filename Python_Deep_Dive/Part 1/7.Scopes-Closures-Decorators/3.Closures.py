## Closures ##
# Let's examine that concept of a cell to create an indirect reference for variables that are in multiple scopes.
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

fn = outer()

print(fn.__code__.co_freevars)
# As we can see, x is a free variable in the closure.

print(fn.__closure__)
# Here we see that the free variable x is actually a reference to a cell object that is itself a reference to a string object.

# Let's see what the memory address of x is in the outer function and the inner function. To be sure string interning does not play a role, I am going to use an object that we know Python will not automatically intern, like a list.

def outer():
    x = [1, 2, 3]
    print('outer:', hex(id(x)))
    def inner():
        print('inner:', hex(id(x)))
        print(x)
    return inner

fn = outer()
print(fn.__closure__)
fn()

# As you can see, each the memory address of x in outer, inner and the cell all point to the same object.

## Modifying the Free Variable ## 
def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count
    return inc


c = counter()

print(c())

print(c())

print(c())

## Shared Extended Scopes ##

def outer():
    count = 0

    def increment1():
        nonlocal count
        count += 1
        return count
    
    def increment2():
        nonlocal count
        count += 2
        return count
    
    return increment1, increment2

inc1, inc2 = outer()

print(inc1())

print(inc1())

print(inc2())

## Multiple Instances of Closures ##
# Recall that every time a function is called, a new local scope is created.

from time import perf_counter

def func():
    x = perf_counter()
    print(x, id(x))

func()

func()

# We can use the feature to create dynamic functions

def pow(n):
    
    def inner(x):
        return x ** n
    return inner

square = pow(2)

print(square(5))

cube = pow(3)

print(cube(5))


# We can see that the cell used for the free variable in both cases is different:
print(square.__closure__)
print(cube.__closure__)

# these two function are different:
print(id(square), id(cube))

## BEWARE #

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
add_4 = adder(4)

print(add_1(1), add_2(2), add_3(3), add_4(4)) # it work as expected!

# But

def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()

print(adders) # these are different function objects.

print(adders[0](10), adders[1](10), adders[2](10), adders[3](10))

# When the lambdas are created their n is the n used in the loop - the same n!!

print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[3].__closure__)
print(hex(id(4))) # address of singleton object 4

# To fix that:

def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step = n: x + step)
    return adders

adders = create_adders()

print(adders[0](10), adders[1](10), adders[2](10), adders[3](10))

# You just need to understand that since the default values are evaluated when the function (lambda in this case) is created, the then-current n value is assigned to the local variable step. So step will not change every time the lambda is called, and since n is not referenced inside the function (and therefore evaluated when the lambda is called), n is not a free variable.

## Nested Closures ##

def incrementer(n):
    def inner(start):
        current = start
        def inc():
            a = 10
            nonlocal current
            current += n
            return current
        return inc
    return inner


fn = incrementer(2)

print(fn)
print(fn.__code__.co_freevars)
print(fn.__closure__)

inc = fn(100)

print(inc)
print(inc.__code__.co_freevars)
print(inc.__closure__)

print(inc())

print(inc())

inc1 = incrementer(3)(200)

print(inc1())

print(inc1())