from collections import namedtuple

data_dict = dict(key1=100, key2=200, key3=300)

Data = namedtuple('Data', data_dict.keys())

print(Data._fields)

# We could try the following (bad idea):

d1 = Data(*data_dict.values())

print(d1)

# it work, but try:

data_dict_2 = dict(key1=100, key3=300, key2=200)

d2 = Data(*data_dict_2.values())

print(d2) # wrong value

# Instead, we should unpack the dictionary itself, resulting in keyword arguments that will be passed to the Data constructor:
d2 = Data(**data_dict_2)
print(d2)

data_dict = dict(first_name='John', last_name='Cleese', age=42, complaint='dead parrot')

print(data_dict.keys())

print(sorted(data_dict.keys()))

Struct = namedtuple('Struct', sorted(data_dict.keys()))

print(Struct._fields)

d1 = Struct(**data_dict)

print(d1)

print(d1.complaint)

print(data_dict['complaint'])

key_name = 'age'
getattr(d1, key_name)

print(data_dict.get('age', None), data_dict.get('invalid_key', None))
print(getattr(d1, 'age', None), getattr(d1, 'invalid_key', None))

data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2':6, 'key3': 7},
    {'key2': 100},
]

def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

print(tuplify_dicts(data_list))