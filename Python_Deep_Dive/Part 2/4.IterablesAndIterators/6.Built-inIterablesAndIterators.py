r_10 = range(10)

print(r_10 is iter(r_10)) # range is an iterable

print(list(r_10))

z = zip([1, 2, 3], 'abc') # zip is an iterator
print(z is iter(z))
print(list(z))
print(list(z))

with open('cars.csv') as f:
    print(type(f))
    print(f is iter(f))
    print(next(f))
    print(f.__next__())
    print(f.readline())

# we can iterate over all the lines using for loops
with open('cars.csv') as f:
    for row in f:
        print(row, end='')

# The TextIOWrapper class also provides a method readlines() 
with open('cars.csv') as f:
    l = f.readlines()

print(l)

origins = set()
with open('cars.csv') as f:
    rows = f.readlines()

for row in rows[2:]:
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)

print(origins)

origins = set()
with open('cars.csv') as f:
    next(f), next(f)
    for row in f:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)

print(origins)

e = enumerate('Python rocks!')

print(e is iter(e))
print(list(e))
print(list(e))