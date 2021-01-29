from Polygons import Polygon

class Polygons:
    def __init__(self, limit, R):
        if limit < 3:
            raise ValueError('Limit must be >= 3.')
        self._limit = limit
        self._R = R
        self._polygons = [Polygon(i, self._R) for i in range(3, limit + 1)]
    
    def __len__(self):
        return self._limit - 2
    
    def __repr__(self):
        return f'Polygons (limit={self._limit}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def highest_area_perimeter_ratio(self):
        return max(self._polygons, key=lambda x: x.area / x.perimeter)

polygons = Polygons(10, 1)

print(polygons[1])

print(polygons.highest_area_perimeter_ratio)

print([p.area / p.perimeter for p in polygons])