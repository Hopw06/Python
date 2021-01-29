# How we cam creaye decorators with parameters #
# We do not directly create a decorator, instead we use an outer function that returns a decorator when called, and pass arguments to that outer function, which the decorator and its inner function can of course access as nonlocal (free) variables.

def dec_factory(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            print('free variables: ', a, b)
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_factory(10, 20)
def my_func():
    print('python rocks')

my_func()

# Let's try with an example
# we wanted our timing decorator to run a number of loops which could be specified as a parameter when decorating the function we want to time.

from functools import wraps

def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                rs = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_elapsed = total_elapsed / num_reps
            print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_elapsed, num_reps))

            return rs
        return inner
    return decorator

def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

@timed(5)
def cal_fib(n):
    return fib(n) 

cal_fib(30)