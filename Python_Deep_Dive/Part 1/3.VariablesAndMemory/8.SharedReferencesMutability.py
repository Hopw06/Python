# setup two variable refer to the same address.
my_var_1 = 'hello'
my_var_2 = my_var_1
print(my_var_1)
print(my_var_2)
print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

my_var_2 = my_var_2 + ' world!' # my_var_2 variable refer to other object.
print(my_var_1)
print(my_var_2)
print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

# with list
my_list_1 = [1, 2, 3]
my_list_2 = my_list_1
print(my_list_1)
print(my_list_2)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

my_list_2.append(4) # this operator perform on same object.

# my_list_1 will also change
print(my_list_1)
print(my_list_2)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

my_list_2 = my_list_2 + [5] # this operator will create new list, my_list_2 will refer to another object/ another memory address.

print(my_list_1)
print(my_list_2)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

############################################################################################################
########################## Behind the scenes with Python's memory manager ##################################

a = 10
b = 10
print("Memory address of a and b: ")
print(hex(id(a)))
print(hex(id(b)))
# a and b are same memory address.
# because integer object are immutable so it's safe for Python.
# The only way to change the value of b is make b refer to another integer object.

b += 5
print("a, b = ", a, b)
print(hex(id(a)))
print(hex(id(b)))

# for mutable object, even they have same contents. Python does not make it same memory address.
my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

# because list has some operators can perform in place, such as append...
