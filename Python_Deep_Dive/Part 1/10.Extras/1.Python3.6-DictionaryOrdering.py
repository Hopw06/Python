from sys import version_info

print(version_info)

# based on the order in which new keys are added into or removed from the dictionary
d = {'a': 1, 'b': 2}

print(d.keys(), d.values(), d.items())

d['x'] = 3

print(d.keys(), d.values(), d.items())

del d['b']

d['b'] = 4

print(d.keys(), d.values(), d.items())

d['x'] = 100

print(d.keys(), d.values(), d.items())

print(d.popitem())

d1 = {'a': 1, 'b': 200}
d2 = {'a': 100, 'd':300, 'c': 400}

d1.update(d2)
print(d1)

# move to end
d = {'a': 1, 'b': 2, 'c': 3}
print('start:', d)
d['a'] = d.pop('a')
print('moved a to end:', d)

# move to front
d = {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
print('start:', d)
d['c'] = d.pop('c')
print('moved c to end:', d)

for i in range(len(d) - 1):
    key = next(iter(d.keys()))
    d[key] = d.pop(key)
print('moved c to front:', d)

# pop last item
d = {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
print('start:', d)
d.popitem()
print('pop last item:', d)

# pop first item
d = {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
print('start:', d)
key = next(iter(d.keys()))
d.pop(key)
print('pop first item:', d)