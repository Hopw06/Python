def process(s):
    print("initial s = {0}, # = {1}".format(s, hex(id(s))))
    s = s + " world" # change to new string object
    print("s after change s = {0}, # = {1}".format(s, hex(id(s))))

my_s = 'hello'
print(my_s)
print('my_s # = {0}'.format(hex(id(my_s))))

process(my_s)

# Check s again
print(my_s)
print('my_s # = {0}'.format(hex(id(my_s))))

# The original my_s is not changed (value and address)
# The copy variable s inside process function did change. It point to new memory address.

# Let's see how this works with mutable objects:
def modify_list(items):
    print('initial items = {0}, address = {1}'.format(items, hex(id(items))))
    if len(items) > 0:
        items[0] = items[0] ** 2 
    items.pop()
    items.append(5)
    # all operator here just change the internal element of list. So memory address is not changed
    # just use try with concat in other function.
    print('after change items = {0}, address = {1}'.format(items, hex(id(items))))

list1 = [2, 3, 4]
print(list1)
print(hex(id(list1)))

modify_list(list1) # modify the internal element of list

print(list1)
print(hex(id(list1)))
# list1 value changed, but the memory address is not changed.
# list1 and items inside modify_list function is both refer to same memory address (object).


def concat_list(items):
    print('initial items = {0}, address = {1}'.format(items, hex(id(items))))
    items = items + [4] # create new list and append items and [4] to it. Then reassign to items.
    # items variable refer to another object, but the original object outside function is not changed.
    print('after change items = {0}, address = {1}'.format(items, hex(id(items))))

list2 = [1, 2, 3]
print(list2)
print(hex(id(list2)))

concat_list(list2)

print(list2)
print(hex(id(list2)))
# list2 (value and address) is not changed. It is same with process function case with string.

