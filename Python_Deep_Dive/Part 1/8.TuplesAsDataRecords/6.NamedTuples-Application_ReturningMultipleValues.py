from random import randint, random

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

color = random_color()
print(color)
print('red={0} green={1} blue={2} alpha={3}'.format(color[0], color[1], color[2], color[3]))

# but nicer
from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue', 'alpha'])

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = randint(0, 255)
    return Color(red, green, blue, alpha)

color = random_color()

print(color)