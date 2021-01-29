import random

print(help(random.random))

print(random.random())

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(sorted(l, key=lambda x: random.random()))

print(''.join(sorted('abcdefgh', key=lambda x: random.random())))