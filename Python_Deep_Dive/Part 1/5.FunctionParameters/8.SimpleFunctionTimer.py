## A simple function timer ##
import time

def time_it(fn, *args, rep = 5, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 3, sep='-')

time_it(print, 1, 2, 3, sep='-', end='*\n', rep=100)

# make function to time the function we pass to and return the average time:

def time_it(fn, *args, rep = 5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep

# Compute powers 
def compute_powers_1(n, *, start=1, end):
    #using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]

def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n**i for i in range(start, end))

# Test
print(compute_powers_1(2, end=5))
print(compute_powers_2(2, end=5))
print(compute_powers_3(2, end=5))

# Check time
print(time_it(compute_powers_1, n = 2, end = 20000, rep=4))

print(time_it(compute_powers_2, n = 2, end = 20000, rep=4))

print(time_it(compute_powers_3, n = 2, end = 20000, rep=4))