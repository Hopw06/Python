s = 'I sleep all night, and I work all day'
iter_s = iter(s)

print(type(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))

from collections import namedtuple

def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)

def cast_row(data_types, data_row):
    return [cast(data_type, value) for data_type, value in zip(data_types, data_row)]

with open('cars.csv') as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')
    cars_data = [cast_row(data_types, line.strip('\n').split(';')) for line in file_iter]
    cars = [Car(*item) for item in cars_data]

print(cars)    
