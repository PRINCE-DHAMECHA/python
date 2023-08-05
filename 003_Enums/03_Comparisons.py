# importing enum for enumerations
from enum import Enum

# creating enumerations using class


class Animal(Enum):
    dog = 1
    cat = 2
    lion = 3


# * Comparison using "is"
if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")

# * Comparison using "!="
if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")
