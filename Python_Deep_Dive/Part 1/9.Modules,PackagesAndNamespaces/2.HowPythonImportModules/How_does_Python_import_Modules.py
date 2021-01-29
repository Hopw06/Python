import sys

# where is Python installed?
print(sys.prefix)

# where are the compiled C binaries located?
print(sys.exec_prefix)

# Where does Python look for imports?

print(sys.path)

# Basically when we import a module, Python will search for the module in the paths contained in sys.path.

# If it does not find the module in one of those paths, the import will fail.


# At a high level, this is how Python imports a module from file:

    # checks the sys.modules cache to see if the module has already been imported - if so it simply uses the reference in there, otherwise:
    # creates a new module object (types.ModuleType)
    # loads the source code from file
    # adds an entry to sys.modules with name as key and the newly created
    # compiles and executes the source code

# One thing that's really to important to note is that when a module is imported, the module code is executed.