from collections import namedtuple

## modifying ##
Point2D = namedtuple('Point2D', ('x', 'y'))

origin = Point2D(10, 0)

# origin.x = 0 # error, because tuple is imutable.

# We could do it as follows:
origin = Point2D(0, origin.y)
print(origin)

Stock = namedtuple('Stock', 'symbol year month day open high low close')

dija = Stock('Dija', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
# to update value of close, we have to
dija = Stock(dija.symbol, dija.year, dija.month, dija.day, dija.open, dija.high, dija.low, 26_394)

# => that was quite paintful!
# more clever by using unpacking.
*value, _ = dija
dija = Stock(*value, 26_394)

# But this approach does not always work, what happens if we want to change a values somewhere in the middle? Or two values?

# We cannot do: *first, month, *last = djia

# That would make no sense whatsoever! (and Python will tell you so!)

# Maybe slicing and unpacking can work here...

print(dija[:3] + (26,) + dija[4:])
dija = Stock(*(dija[:3] + (26,) + dija[4:]))
print(dija)

values = dija[0:1] + (2019,) + dija[2:3] + (26,) + dija[4:]
dija = Stock(*values)

print(dija)
# Fortunately there's a better way!

print(dija)
print(id(dija))

dija = dija._replace(year=2019, month=26)

print(dija)
print(id(dija))

## extending named tuples
# change from 2D
Point2D = namedtuple('Point2D', ('x', 'y'))
# to
Point3D = namedtuple('Point3D', ('x', 'y', 'z'))


# But if our named tuple has many fields, such as our Stock named tuple that's a little more difficult:
print(dija)

# Suppose we want to create a new class, say StockExt, it would take some effort:
StockExt = namedtuple('StockExt', '''symbol year month day open high low
                                    close previous_close''')

print(StockExt._fields)

# we can extend our Stock class to do it

StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))

print(StockExt._fields)

StockExt = namedtuple('StockExt', ' '.join(Stock._fields) + ' previous_close')

print(StockExt._fields)

dija_ext = StockExt(*dija, 25_000)
print(dija_ext)

dija_ext = StockExt._make(dija + (25_000, ))
print(dija_ext)