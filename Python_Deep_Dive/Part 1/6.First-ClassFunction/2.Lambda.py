## Assigning to Variable ##
func = lambda x: x**2

print(type(func))

print(func(3))

# We can specify arguments for lambdas just like we would for any function created using def, except for annotations:
func_1 = lambda x, y = 10: (x, y)

print(func_1(1))

print(func_1(1, 2))

# We can even use * and **:
func_2 = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})

print(func_2(1, 'a', 'b', y=100, a=10, b=20))

## Passing as arguments ##
def apply_func(x, fn):
    return fn(x)

print(apply_func(10, lambda x: x**x))
print(apply_func(10, lambda x: 10**x))

# Of course we can make this even more generic:
def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print(apply_func(lambda x, y: x + y, 1, 2))

print(apply_func(lambda x, *, y: x * y, 1, y = 2))

print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5, 5))

# Other way:
print(apply_func(sum, (1, 2, 3, 4, 5)))

def multiply(x, y):
    return x * y

print(apply_func(multiply, 'a', 5))

print(apply_func(lambda x, y: x * y, 'a', 5))