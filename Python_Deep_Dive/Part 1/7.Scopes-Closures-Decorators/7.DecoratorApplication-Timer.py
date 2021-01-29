def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args = [str(a) for a in args]
        kwargs = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        all_args = args + kwargs
        args_str = ', '.join(all_args)

        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, args_str, elapsed))

        return result

    return inner

# Let's test with fibonacci number:
## using Recursion ##
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    return calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)

@timed
def fib_recursed(n):
    return calc_recursive_fib(n)

print(fib_recursed(33))

print(fib_recursed(34))

print(fib_recursed(35))

## using a Loop ##
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1

    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(fib_loop(33))

print(fib_loop(34))

print(fib_loop(35))

## Using Reduce ##

# reduce() is roughly equivalent to the following Python function:
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

from functools import reduce

def fib(prev, n):
    return (prev[0] + prev[1], prev[0])

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n - 1)
    fib_n = reduce(fib, dummy, initial)
    return fib_n[0]

print(fib_reduce(33))

print(fib_reduce(34))

print(fib_reduce(35))

### compare ###
print(fib_recursed(35))
print(fib_loop(35))
print(fib_reduce(35))

for i in range(10):
    result = fib_loop(10000)

for i in range(10):
    result = fib_reduce(10000)