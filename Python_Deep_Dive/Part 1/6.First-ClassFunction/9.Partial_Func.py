from functools import partial

def my_func(a, b, c):
    print(a, b, c)

f = partial(my_func, 10)
f(20, 30)

# We could have done this using another function (or a lambda) as well:

def partial_func(b, c):
    return my_func(10, b, c)

partial_func(20, 30)

fn = lambda b, c: my_func(10, b, c)
fn(20, 30)

# Any of these ways is fine, but sometimes partial is just a cleaner more consise way to do it.

# Also, it is quite flexible with parameters:
def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

f = partial(my_func, 10, k1 = 'a')
f(20, 30, 40, k2 = 'b', k3 = 'c')

# We can do it with regular function as well:

def partial_func(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1 = 'a', k2 = k2, **kwargs)

partial_func(20, 30, 40, k2 = 'b', k3 = 'c')

# As you can see in this case, using partial seems a lot simpler.

# Also, you are not stuck having to specify the first argument in your partial:
def power(base, exponent):
    return base ** exponent

print(power(2, 3))

square = partial(power, exponent=2)

print(square(4))

cube = partial(power, exponent=3)

print(cube(2))

print(cube(base=3))

## Caveat
# We can certainly use variables instead of literals when creating partials, but we have to be careful.
def my_func(a, b, c):
    print(a, b, c)

a = 10
f = partial(my_func, a)

f(20, 30)

# Now let's change the value of the variable a and see what happens:
a = 100

f(20, 30)

# As you can see, the value for a is fixed once the partial has been created.

# In fact, the memory address of a is baked in to the partial, and a is immutable.

# If we use a mutable object, things are different:

a = [10, 20]
f = partial(my_func, a)

f(100, 200)

a.append(30) # because this operator is performed on the same memory address
f(100, 200) 

# if you point a to other list object

a = [1,2,3] 
f(100, 200) # it will not change

## Use Cases ##
# We tend to use partials in situation where we need to call a function that actually requires more parameters than we can supply.

# Often this is because we are working with exiting libraries or code, and we have a special case.

# For example, suppose we have points (represented as tuples), and we want to sort them based on the distance of the point from some other fixed point:

origin = (0, 0)
l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

dist2 = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

print(dist2(origin, (1, 1)))

print(sorted(l, key = lambda x: dist2(x, origin)))
print(sorted(l, key = partial(dist2, origin)))

## Error ## 

print(cube(2))

print(cube(2, 4)) # error