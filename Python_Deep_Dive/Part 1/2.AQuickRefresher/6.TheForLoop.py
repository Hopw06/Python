# In Python, an iterable is an object capable of returning values one at a time.
# Many object in Python are iterable: lists, strings, file object and many more.

# THE FOR LOOP IN OTHER LANGUAGES SUCH AS C/C++, JAVA IS NOT EQUAL TO FOR LOOP IN PYTHON
# The for statement is a way to iterate over iterables/ to user for loop in Python, we require an iterable object to work with.

# A simple iterable object is generated via the range() function.
for i in range(5):
    print(i)

# Many object are iterable in Python:
for x in [1, 2, 3]: # list
    print(x)

for x in 'hello': # string
    print(x)

for x in ('a', 'b', 'c'): # set
    print(x)

# break/ continue
for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

# else clause
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')

# break, continue in the try statement same as while loop (finally statement always executes)

for i in range(5):
    print('--------------------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always runs')
    print(i)

# There are a number of standard techniques to iterate over iterables:

s = 'hello'
for c in s:
    print(c)

# sometimes, we want to know index of item in loop:
s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1

# better

for i in range(len(s)):
    print(i, s[i])

# even better

for i, c in enumerate(s):
    print(i, c)