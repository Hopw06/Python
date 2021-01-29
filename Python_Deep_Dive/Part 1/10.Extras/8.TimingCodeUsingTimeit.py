from timeit import timeit

import math
print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

# print(timeit(stmt='math.sqrt(2)')) # error

# 1
print(timeit(stmt='import math\nmath.sqrt(2)'))

#2
print(timeit(stmt='math.sqrt(2)', setup='import math'))

#3
print(timeit(stmt='math.sqrt(2)', globals=globals()))

# come with setup approach
rs1 = timeit(stmt='math.sqrt(2)', setup='import math')
rs2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')

print(f'Result 1 = {rs1}')
print(f'Result 2 = {rs2}')

# global and local name space
import random
l = random.choices(list('python'), k = 500)

print('l' in globals())
print('l' in locals())

print(timeit(stmt='random.choice(l)', setup='import random', globals=globals()))

def random_choices():
    randoms = random.choices(list('python'), k = 500)

    return timeit(stmt='random.choice(randoms)', setup='import random', globals=locals())

print(random_choices())