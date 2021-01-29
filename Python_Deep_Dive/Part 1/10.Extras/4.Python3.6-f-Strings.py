# f-Strings is short for formatted string literals
# format string method

# using {}
print('{} % {} = {}'.format(10, 3, 10 % 3))

# using {number}
print('{1} % {2} = {0}'.format(10 % 3, 10, 3))

# using {name}
print('{a} % {b} = {mod}'.format(a=10, b=3, mod=10 % 3))

# But now we can also do this:
a = 10
b = 3
print(f'{a} % {b} = {a % b}')

a = 10 / 3
print(f'{a:0.5f}')

name = 'Python'
print(f'{name} rocks!')

def outer():
    name = 'Python'

    def inner():
        return f'{name} rocks!'
    
    return inner

print(outer()())

sq = lambda x: x**2
a = 10
b = 1

print(f'{sq(a) if b > 5 else a}')

b = 10
print(f'{sq(a) if b > 5 else a}')

# or even this:
a = 10
b = 1

print(f'{(lambda x: x**2)(a) if b > 5 else a}')

b = 10
print(f'{(lambda x: x**2)(a) if b > 5 else a}')