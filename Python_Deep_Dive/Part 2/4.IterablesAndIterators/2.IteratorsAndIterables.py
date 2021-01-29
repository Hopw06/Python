class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
    
    def __len__(self):
        return len(self._cities)
    
    def __iter__(self):
        print('Calling Cities instance __iter__')
        return self.CityIterator(self)
    
    def __getitem__(self, s):
        return self._cities[s]
    
    class CityIterator:
        def __init__(self, city_obj):
            print('Calling CityIterator __init__')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('Calling CityIterator instance __iter__')
            return self
        
        def __next__(self):
            if self._index >= len(self._city_obj._cities):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

cities = Cities()
for city in cities:
    print(city)

print(cities[0])

print(next(iter(cities)))