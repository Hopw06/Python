import random

for _ in range(10):
    print(random.randint(10, 20), random.random())
print("----------------------------------------------------------------")

for _ in range(10):
    print(random.randint(10, 20), random.random())

print("----------------------------------------------------------------")
random.seed(0)
for _ in range(10):
    print(random.randint(10, 20), random.random())

print("----------------------------------------------------------------")
for _ in range(10):
    print(random.randint(10, 20), random.random())

print("----------------------------------------------------------------")
random.seed(0)
for _ in range(10):
    print(random.randint(10, 20), random.random())

def generate_random_stuff(seed=None):
    random.seed(seed)
    result = []

    for _ in range(5):
        result.append(random.randint(0, 5))
    
    characters = ['a', 'b', 'c']
    random.shuffle(characters)
    result.append(characters)

    for _ in range(5):
        result.append(random.gauss(0, 1))
    
    return result

print(generate_random_stuff())
print(generate_random_stuff())

print(generate_random_stuff(0))
print(generate_random_stuff(0))

print(generate_random_stuff(100))
print(generate_random_stuff(100))

def freq_analysis(lst):
    return {k: lst.count(k) for k in set(lst)}

lst = [random.randint(0, 10) for _ in range(100)]
print(lst)

random.seed(0)
print(freq_analysis(lst))

random.seed(0)
print(freq_analysis([random.randint(0, 10) for _ in range(1_000_000)]))

# built-in funtion for counting
from collections import Counter

random.seed(0)
c = Counter([random.randint(0, 10) for _ in range(1_000_000)])
print(c)