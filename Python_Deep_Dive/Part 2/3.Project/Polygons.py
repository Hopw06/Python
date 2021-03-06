import math

class Polygon:
    def __init__(self, vertexs, circumradius):
        if vertexs < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._vertexs = vertexs
        self._circumradius = circumradius
    
    def __str__(self):
        return f'Polygon(vertexs={self._vertexs}, circumradius={self._circumradius})'
    
    @property
    def count_vertices(self):
        return self._vertexs
    
    @property
    def count_edges(self):
        return self._vertexs
    
    @property
    def circumradius(self):
        return self._circumradius

    @property
    def interior_angle(self):
        return 180 - (360 // self._vertexs)
    
    @property
    def side_length(self):
        return 2 * self._circumradius * math.sin(math.pi / self._vertexs)
    
    @property
    def apothem(self):
        return self._circumradius * math.cos(math.pi / self._vertexs)
    
    @property
    def area(self):
        return self._vertexs * self.side_length * self.apothem * 0.5
    
    @property
    def perimeter(self):
        return self._vertexs * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == self.count_edges and self.circumradius == other.circumradius)
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides:', ' Exception expected, not received')
    except ValueError:
        pass
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(vertexs=3, circumradius=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                    f' expected: {n}')
    assert p.count_edges == n, (f'actual: {p.count_edges},' f' expected: {n}')
    assert p.circumradius == R, (f'actual: {p.circumradius}, expected: {R}')
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},', f' expected: 60')

    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle},', f'expected: 90')
    assert p.area == 2.0, (f'actual: {p.area},', f'expected: 2.0')

    assert math.isclose(p.side_length, math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol), (f'actual: {p.side_length},', f'expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol), (f'actual: {p.perimeter},', f'expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol), (f'actual: {p.perimeter},', f'expected: 0.707')

    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12.0, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120, rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635, rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150, rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

test_polygon()