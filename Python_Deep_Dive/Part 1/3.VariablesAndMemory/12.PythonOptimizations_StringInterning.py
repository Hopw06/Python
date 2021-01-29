# Python will also intern string literals that look like indentifiers.
# But it's also tested in Python shell.
a = 'hello'
b = 'hello'

print(a is b)

#but 
a = 'hello, world!'
b = 'hello, world!'

print(a is b) # in Python shell, it will return false.

# even in Python shell
# the test below will return true

a = "hello_worl_i_am_a_programer"
b = "hello_worl_i_am_a_programer"

print(a is b) # because a & b look like indentifiers.

# AGAIN, THE PYTHON PARSER WILL ANALYSE THE SOURCES CODE FILE AND FIND OUT WHETHER THERE ARE VARIABLES WITH SAME VALUE, AND MAKE IT SINGLETON. 
# THIS WILL MAKE COMPARING FASTER.

# We can intern strings by using sys.intern() function.
def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    print("a address: " + hex(id(a)))
    print("b address: " + hex(id(b)))
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is interned' * 200)
    b = sys.intern('a long string that is interned' * 200)
    print("a address: " + hex(id(a)))
    print("b address: " + hex(id(b)))
    for i in range(n):
        if a is b:
            pass

import sys
import time

start = time.perf_counter()
compare_using_equals(1000000)
end = time.perf_counter()

print("eq: ", end - start)


start = time.perf_counter()
compare_using_interning(1000000)
end = time.perf_counter()

print("identity: ", end - start)
