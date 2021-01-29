# Logger, Stacked Decorators
def logger(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(fn.__name__, run_dt))
        return result
    return inner

@logger
def func_1():
    pass

@logger
def func_2():
    pass

func_1()

func_2()

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end - start))
        return result
    
    return inner

@timed
@logger # timed(logger(factorial))
def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))

factorial(10)

@logger
@timed # timed(logger(factorial))
def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))

factorial(10)

def dec_1(fn):
    def inner():
        print('running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('running dec_2')
        return fn()
    return inner

@dec_1
@dec_2 # dec_1(dec_2(my_func))
def my_func():
    print('running my_func')

my_func()