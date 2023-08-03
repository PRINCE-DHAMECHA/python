import numpy as np
from collections import defaultdict

# * Data types are nothing but variables you use to reserve some space in memory. Python variables do not need an explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable.

# ~ Built-in types

# * 1. Boolean

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
print(a, type(a))  # 5817252738.123123
a = 100.e2
print(a)  # 10000.0
a = 103123.e35
print(a, type(a))  # 1.03123e+40
a = 103123055045401005
print(a, type(a))  # 1.03123e+40

# ^ (III) Complex Number:-

#! The <, <=, > and >= operators will raise a TypeError exception when any operand is a complex number.
a = 2 + 1j
print(a)

# * 3. Strings
# String are identified as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Strings are immutable sequence data type, i.e each time one makes any changes to a string, completely new string object is created.

# str: a unicode string. The type of 'hello'
print(type('hello'))  # <class 'str'>

# bytes: a byte string. The type of b'hello'
print(type(b'hello'))  # <class 'bytes'>

a = reversed('hello')
print(*a)

# * 4. Sequences and collections

# ^ (I) String: Already discussed

# ^ (II) A tuple is similar to a list except that it is fixed-length and immutable. So the values in the tuple cannot be changed nor the values be added to or removed from the tuple. Tuples are commonly used for small collections of values that will not need to change, such as an IP address and port. Tuples are represented with parentheses instead of square brackets:

a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
# b[2] = 'something else'  #! TypeError: 'tuple' object does not support item assignment
print(b[2])

# A tuple with only one member must be defined(note the comma) this way:
one_member_tuple = ('Only member')
print(type(one_member_tuple))  # str
one_member_tuple = ('Only member',)
print(type(one_member_tuple))  # tuple
one_member_tuple = 'Only member',  # No brackets
print(type(one_member_tuple))  # tuple

# ^ (III) list: The list type is probably the most commonly used collection type in Python. Despite its name, a list is more like an array in other languages, mostly JavaScript. In Python, a list is merely an ordered collection of valid Python values. A list can be created by enclosing values, separated by commas, in square brackets:

a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
# List is mutable
b[2] = 'something else'  # allowed
print(b)
print(a*2)  # will give a's element twice
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
# * 2nd last
print(nested_list[-2])
nested_list.append('prince')
nested_list.insert(1, 'Batman')
print(nested_list)
print(nested_list.index('prince'), len(
    nested_list), nested_list.count('prince'))
# ! Error
# print(nested_list.index('pri'))
nested_list.reverse()
print(nested_list.pop())
print(nested_list)


# ^ (IV) Set: A set is a collection of elements with no repeats and without insertion order but sorted order. They are used in situations where it is only important that some things are grouped together, and not what order they were included. For large groups of data, it is much faster to check whether or not an element is in a set than it is to do the same for a list.

a = {1, 2, 'a', 2}
print(a)  # {1, 2, 'a'}
if 2 in a:
    print("Yes we found the victim :)")

# ~ FrozenSet

frz = frozenset({1, 2, 3, 4, 1})
print(frz)
frz = frozenset('fdsfsdf')
print(frz)
frz = frozenset([1, 3, 1, 23, 1, 23])
print(frz)
frz = frozenset((1, 3, 1, 23, 1, 23))
print(frz)
# frz = frozenset(1)  # ! TypeError: 'int' object is not iterable


# ^ (V) dict : A dictionary in Python is a collection of key-value pairs. The dictionary is surrounded by curly braces. Each pair is separated by a comma and the key and value are separated by a colon. Here is an example:

a = {1: 'one', 2: 'two', 'five': '5'}
print(a['five'])
# print(a['f'])  # ! Error

# ?  To resolve this use defaultDict as shown
b = defaultdict(lambda: 'default', a)
print(b["fivee"], b["five"])

print(b.keys())
print(b.values())

# * Loop over dict:
for k in a.keys():
    print('{} is {}'.format(a[k], k))


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
