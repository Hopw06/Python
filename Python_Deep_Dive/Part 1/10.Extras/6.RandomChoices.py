# How would you pick a random element from a list?
import random

random.seed(0)
l = [10, 20, 30, 40, 50, 60]

random_index = random.randrange(len(l))

print(l[random_index])

random.seed(0)
for i in range(10):
    print(l[random.randrange(len(l))])

# using choice
random.seed(0)
for _ in range(10):
    print(random.choice(l))

list_1 = list(range(1000))

random.seed(10)
print(random.choices(list_1, k = 5))

for _ in range(5):
    print(random.choices(list_1, k = 3))

# Now the thing about choices is that it does the selection with replacement.

list_2 = ['a', 'b', 'c']

random.seed(0)
for _ in range(10):
    print(random.choices(list_2, k = 2))

for _ in range(10):
    print(random.choices(list_2, k = 5))

# In addition, we can also specify a weight for each item in the population.

weights_2 = [10, 1, 1]

for _ in range(10):
    print(random.choices(list_2, k = 5, weights=weights_2))

weights_2 = [100, 1, 1]

for _ in range(10):
    print(random.choices(list_2, k = 5, weights=weights_2))