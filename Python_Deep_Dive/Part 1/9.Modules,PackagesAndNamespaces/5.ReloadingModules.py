# create a module file
import os

def create_module_file(module_name, **kwargs):
    module_file_name = '{0}.py'.format(module_name)
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write('# {0}.py\n\n'.format(module_name))
        f.write("print('running {0}...')\n\n".format(module_name))
        f.write('def print_values():\n')
        for key, value in kwargs.items():
            f.write("\tprint('{0}', '{1}')\n".format(key, value))

create_module_file('test', k1=10, k2='python')

import test

print(test)

test.print_values()

create_module_file('test', k1=10, k2='python', k3='cheese')

test.print_values() # nothing changed

print(id(test))

# try to re-import it

import test

print(id(test))
print(test)

test.print_values()

# The module object is the same one we initially loaded - our namespace and sys.modules still points to that old one. Somehow we have to force Python to reload the module.
import sys
del sys.modules['test']

import test
test.print_values()
print(id(test))

# other way:
print(id(test))
test.print_values()

create_module_file('test', k1=10, k2='python', k3='cheese', k4='parrots')

import importlib
importlib.reload(test)

print(test)
print(id(test))
test.print_values()

# but try
del sys.modules['test']

create_module_file('test', k1='python')
from test import print_values

print_values()

print(id(print_values))

create_module_file('test', k1='python', k2='cheese')

# importlib.reload(test) # error

print('test' in sys.modules)

test = sys.modules['test']

print(test)
test.print_values()
print(id(test.print_values))

importlib.reload(test)

print(id(test.print_values))
print(id(print_values)) # the old function object is not reload.

print_values()
test.print_values()