# Constant Expressions
def my_func():
    a = 24 * 60 # imutable
    b = (1, 2) * 5 # imutable
    c = 'abc' * 3 # imutable
    d = 'ab' * 11 # imutable
    e = 'the quick brown fox ' * 10000 # too long
    f = [1, 2] * 5

print(my_func.__code__.co_consts)

    ## Python pre cache imutable object which not be change. 
    ## From output, you can see f = [1, 2] * 5 not to be cached.

# Membership tests
def my_func1():
    if e in [1, 2, 3]:
        pass

print(my_func1.__code__.co_consts)
# As you can see, mutable list is converted to immutable tuple. 
# Because we testing membership of the list, so it is fine to convert list to immutable set. 
# And immutable tuple is more efficient in testing membership.

def my_func2():
    if e in {1, 2, 3}:
        pass

print(my_func2.__code__.co_consts)

# set => frozenset({1, 2, 3})

# set > tuple > list in membership testing
import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print()
print(char_tuple)
print()
print(char_set)
print()

def membership_test(n, container):
    for i in range(n):
        if 'p' in container:
            pass

start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list membership: ', end - start)

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple membership: ', end - start)

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set membership: ', end - start)

# Because set are basically dictionary-like objects, so hash maps are used for looking up an item to determine membership.