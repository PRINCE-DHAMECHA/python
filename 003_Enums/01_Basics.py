from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


# ^ Color.red
print(Color.red)
print(Color(1))
print(Color['red'])

print(Color.red.name)
print(Color.red.value)
