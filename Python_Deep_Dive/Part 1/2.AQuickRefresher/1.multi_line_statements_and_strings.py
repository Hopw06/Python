# Implicit examples

a = [1, # We can also
    2,  # add comments
    3]  # here

print(a)

# This works the same way for tuples, sets and dictionaries
a = (
    1, # first element
    2, # second element
    3, # third element
)

print(a)

a = {
    1, # one
    2, # two
    3, # three
}

print(a)

a = {
    'key1' : 'value1', # comment
    'key2' : # comment
    'value2' # comment
}

print(a)

# We can also break up function arguments and parameters:

def my_func(a, # some comment
        b, c
    ):
    print(a + b + c)

my_func(1, 2, 3)

# Explicit examples
# You can use the \ character to explicitly create multi-line statements.

a = 10
b = 20
c = 30

if a > 5 \
    and b > 10 \
        and c > 20:
        print("yes!!!")
# The identation in continued-lines does not matter

# Multi-line strings.
a = '''this is
a multi-line string'''

print(a)

# Multi-line comments:

# this is 
# a multi-line
# comment