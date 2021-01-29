# Built-in object types are mutable.
# The internal contents (state) of the object in memory can be modified.

my_list = [1, 2, 3]
print(my_list)
print(hex(id(my_list)))

# append
my_list.append(4)
print(my_list)
print(hex(id(my_list)))

# modified
my_list[0] = 0
print(my_list)
print(hex(id(my_list)))

# concate
my_list = my_list + [4]
print(my_list)
print(hex(id(my_list))) # address did change

# Because it make a new list and append my list and [4] to it.

# similarly with dictionary objects that are also mutable types.
my_dict = dict(key1 = 'value1')
print(my_dict)
print(hex(id(my_dict)))
# modified
my_dict['key1'] = 'value 1'
print(my_dict)
print(hex(id(my_dict)))

# Now consider the immutable sequence type: tuple
# The tuple is immutable, so elements cannot be added, removed or replaced.
# This tuple never change util t variable refer to other object.
t = (1, 2, 3)
print(t)

# But consider the following tuple t:
a = [1, 2]
b = [3, 4]
t = (a, b)

print(t)
print(hex(id(t)))
# t is immutable, but the elements a and b are mutable. So:
# a, b can change
a.append(3)
b.append(5)
b.append(6)

print(t)
print(hex(id(t)))
# but memory address of tuple t is not changed.