import numbers

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = x, y
        else:
            raise TypeError("Point co-ordinates must be real numbers.")
    
    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'
    
    def __len__(self):
        return 2
    
    def __getitem__(self, s):
        return self._pt[s]

p = Point(1, 2)
print(p)
print(len(p))
print(p[0], p[1])
x, y = p
print(x, y)

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []
    
    def __repr__(self):
        pts_str = ', '.join([str(p) for p in self._pts])
        return f'Polygon({pts_str})'
    
    def __len__(self):
        return len(self._pts)
    
    def __getitem__(self, s):
        return self._pts[s]
    
    def __setitem__(self, s, value):
        try:
            rhs = [Point(*pt) for pt in value]
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                raise TypeError('Invalid Point or iterable of Points')
        
        if (isinstance(s, int) and is_single) \
            or (isinstance(s, slice) and not is_single):
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index/slice assignment')
    
    def __add__(self, pt):
        if isinstance(pt, Polygon):
            new_pts = self._pts + pt._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with another Polygon')
    
    def append(self, pt):
        self._pts.append(pt)
    
    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts = self._pts + pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts = self._pts + points
    
    def __iadd__(self, pts):
        self.extend(pts)
        return self

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))
    
    def __delitem__(self, s):
        del self._pts[s]
    
    def pop(self, i):
        return self._pts.pop(i)

p = Polygon((0, 0), [1, 1])
print(p)