# The while loop is a way to repeat a block of code as long as a specified condition is met.
i = 0
while i < 5:
    print(i)
    i += 1

# if the condition is not met, the body inside While will not execute at all. 
# Some other languages hava a concept of do - while, which will execute at least one time. 
# But there is no such thing in Python. But we can do it by using a infinite loop and check the condition inside while.

i = 5
while True:
    print(i)
    if i >= 5:
        break

# This is a standard pattern:
min_length = 2

name = input("Please enter your name:")
while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")
print("Hello, {0}".format(name))

# duplicate code, ask user to input name twice.

while True:
    name = input("Please enter your name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print("Hello, {0}".format(name))

# The continue keyword
a = 0
while a < 10:
    a += 1
    if a % 2:
        continue
    print(a)

# The while loop also can be used with an else clause!!!
# The else statement will be executed when the while loop finish normally, not be break. 
l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)
print(l) # [1, 2, 3, 10]

# Use else statement
l = [1, 2, 3]
val = 10
idx = 0
found = True

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
else:
    l.append(val)
print(l) # [1, 2, 3, 10]

l = [1, 2, 3]
val = 2
idx = 0
found = True

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
else:
    l.append(val)
print(l) # [1, 2, 3]