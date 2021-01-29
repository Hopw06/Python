# Ex1
def counter():
    i = 0
    def inc():
        nonlocal i
        i += 1
        return i
    return inc

cnt = counter()
print(cnt())
print(cnt())

class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel
        # self.is_consumed = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # if self.is_consumed:
        #     raise StopIteration
        # else:
        result = self.counter_callable()
        if result < self.sentinel:
            self.is_consumed = True
            raise StopIteration
        else:
            return result

cnt = counter()
cnt_iter = CounterIterator(cnt, 5)
for c in cnt_iter:
    print(c)

# print(next(cnt_iter))
# help(iter)

# Ex2
import random

random.seed(0)
for i in range(10):
    print(i, random.randint(0, 10))

random_iterator = iter(lambda : random.randint(0, 10), 8)

random.seed(0)
for num in random_iterator:
    print(num)

# Ex3
def countdown(start=10):
    def run():
        nonlocal start
        start -= 1
        return start
    return run

takeoff = countdown(10)
for _ in range(15):
    print(takeoff())

# But we want to able to iterate over it and stop the iteratoon once we reach 0.
takeoff = countdown(10)
takeoff_iter = iter(takeoff, -1)

for val in takeoff_iter:
    print(val)