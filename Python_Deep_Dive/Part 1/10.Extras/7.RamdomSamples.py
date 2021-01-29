import random

# elements can be repeated
print(random.choices(list('abc'), k = 10))

l = range(20)

# use samle function to generate non-repeat number
print(random.sample(l, k = 10))

print(random.sample(l, k = 20))

# print(random.sample(l, k = 50)) # error
random.seed(0)
print(random.sample(l, k=5))

random.seed(0)
print(random.sample(l, k=5))

suits = 'C', 'D', 'E', 'A'
ranks = tuple(range(2, 11)) + tuple('JQKA')

deck = [str(rank) + suit for suit in suits for rank in ranks]
print(deck)

from collections import Counter

print(Counter(random.sample(deck, k = 20)))
print(Counter(random.choices(deck, k = 20)))