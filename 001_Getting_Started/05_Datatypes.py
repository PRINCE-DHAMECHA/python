
# ~ Built-in types

# * 1. Boolean

import numpy as np
print(1 == 1)  # True
print(True and False)  # False
print(True or False)  # True
print(not False)  # True

# ^If boolean values are used in arithmetic operations, their integer values(1 and 0 for True and False) will be used to return an integer result
print(True + True)  # 2
print(True * True)  # 1
print(True + False)  # 1

# * 2. Numbers

# ^ (I) int:-

a = 5817252738123123123123
print(a)

# ^ (II) float:-

a = 5817252738.123123123123
print(a)  # 5817252738.123123
a = 100.e2
print(a)  # 10000.0
a = 103123.e35
print(a)  # 1.03123e+40

# ^ (III) Complex Number:-

#! The <, <=, > and >= operators will raise a TypeError exception when any operand is a complex number.
a = 2 + 1j
print(a)

# * 3. Strings

# str: a unicode string. The type of 'hello'
print(type('hello'))  # <class 'str'>

# bytes: a byte string. The type of b'hello'
print(type(b'hello'))  # <class 'bytes'>

a = reversed('hello')
print(*a)

# * 4. Sequences and collections

# ^ (I) String: Already discussed

# ^ (II) Tuples:  An ordered collection of n values of any type (n >= 0).

a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
# b[2] = 'something else'  #! TypeError: 'tuple' object does not support item assignment
print(b[2])

# ^ (IV) list: An ordered collection of n values (n >= 0)

a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else'  # allowed
print(b)

# ^ (V) Set: An unordered collection of unique values. Items must be hashable.
a = {1, 2, 'a', 2}
print(a)  # {1, 2, 'a'}

# ^ dict : An unordered collection of unique key-value pairs; keys must be hashable
a = {1: 'one', 2: 'two', 'five': '5'}
print(a['five'])

# ~ Built-in Constants

print(True)  # The true value of the built-in type bool
print(False)  # The false value of the built-in type bool

print(None)  # A singleton object used to signal that a value is absent.
# ^ None doesn't have any natural ordering. Using ordering comparison operators (<, <=, >=, >) isn't supported anymore and will raise a TypeError.
# print(None < -32)  # ! Error

# Ellipsis or ...: used in core Python3+ anywhere and limited usage in Python2.7+ as part of array notation. numpy and related packages use this as a 'include everything' reference in arrays.

array = np.random.rand(2, 2, 2, 2)
print(array)
print(array[..., 0])
print(array[Ellipsis, 0])
# ? [:, :, :, 0], [ … , 0] and [Ellipsis, 0] are all equivalent.

# ~ Test Datatypes:

print(type(1))  # <class 'int'>

# * In conditional statements it is possible to test the datatype with isinstance. However, it is usually not encouraged to rely on the type of the variable.

print(isinstance(1, int))


# ~ Conversion:

a = '123.456'
b = float(a)
print(b)
# In this example, you'll get a ValueError because Python cannot directly convert the string '123.456' to an integer. This is because the string '123.456' represents a floating-point number, and converting it directly to an integer would discard the decimal part, leading to potential loss of information.

# The intermediate step of converting to a float is necessary to preserve the decimal part before converting to an integer. By using float(a), you convert the string '123.456' to the floating-point number 123.456, which retains the decimal precision.

# Once you have the floating-point representation, you can then choose to either truncate the decimal part using int() or round it using round():
# c = int(a)  #! ValueError: invalid literal for int() with base 10: '123.456'
c = '123'
e = int(c)  # No error
d = int(b)  # 123
print(e)

a = 'hello'
list(a)  # ['h', 'e', 'l', 'l', 'o']
set(a)  # {'o', 'e', 'l', 'h'}
tuple(a)  # ('h', 'e', 'l', 'l', 'o')


b'foo bar'
# results bytes in Python 3, str in Python 2
u'foo bar'
# results str in Python 3, unicode in Python 2
# 'foo bar':results str
r'foo bar'
# results so called raw string, where escaping special characters is not necessary, everything it taken verbatim as you typed

normal = 'foo\nbar'  # foo
#                      bar
escaped = 'foo\\nbar'  # foo\nbar
raw = r'foo\nbar'  # foo\nbar


# ~ Mutable and Immutable Data Types

# An object is called mutable if it can be changed. For example, when you pass a list to some function, the list can be changed:

def f(m):
    m.append(3)  # adds a number to the list. This is a mutation.


x = [1, 2]
f(x)
print(x == [1, 2])  # False now, since an item was added to the list


# ^ Note that variables themselves are mutable, so we can reassign the variable x, but this does not change the object that x had previously pointed to. It only made x point to a new object.

# * Examples of immutable Data Types:
# int, long, float, complex
# str
# bytes
# tuple
# frozenset

# * Examples of mutable Data Types:
# bytearray
# list
# set
# dict
