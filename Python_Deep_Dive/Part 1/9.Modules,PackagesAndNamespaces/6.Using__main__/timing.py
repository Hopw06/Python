# timing.py
"""
Times how long a snippet of code takes to run
over multiple iterations
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'repeat elapsed average')

def timeit(code, repeat=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeat):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeat
    return Timing(repeat, average, average)

if __name__ == '__main__':
    # get code from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help='The Python code snippet to be timed.')
    parser.add_argument('-r', '--repeats', type=int, default=10, help='Number of time to repeat the test.')
    args = parser.parse_args()
    print('timing: {0}...'.format(args.code))
    print(timeit(code=str(args.code), repeat=args.repeats))