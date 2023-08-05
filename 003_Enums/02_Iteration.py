from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


for c in Color:
    print(c.name, c.value)
