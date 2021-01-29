import sys

print(sys.exec_prefix)

import importlib

print(importlib.__file__)

print(importlib)

fractions = importlib.import_module('fractions')

f = fractions.Fraction(2, 3)

print(f)

print(fractions)

import math

print(math)
# To import
# Conceptually Python divides the work between finders and loaders.
# The finders are responsible for finding the module/package and returning the module spec, while the loaders, are responsible for "loading" the source code that is then used in the final steps to compile, execute and cache the module object. An object that implements both is called an importer - but they are still two separate concepts.
# Here are the finders currently registered on my system:

print(sys.meta_path)

# We can also use importlib to find the spec for a particular module:
print(importlib.find_loader('math'))

print(importlib.find_loader('fractions'))

with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py...')\n")
    code_file.write("a = 100\n")

print(importlib.find_loader('module1'))

import module1

print(module1.a)

# create a module in other path
import os

file_abs_path = os.path.join("F:\Test", 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write("x = 'python'\n")

# print(importlib.util.find_spec('module2')) NoneType

sys.path.append("F:\Test")

print(importlib.find_loader('module2'))

import module2

print(module2.x)