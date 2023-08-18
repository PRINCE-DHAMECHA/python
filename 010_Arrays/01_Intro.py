# Parameter        Details
# b                Represents signed integer of size 1 byte
# B                Represents unsigned integer of size 1 byte
# c                Represents character of size 1 byte
# u                Represents unicode character of size 2 bytes
# h                Represents signed integer of size 2 bytes
# H                Represents unsigned integer of size 2 bytes
# i                Represents signed integer of size 2 bytes
# I                Represents unsigned integer of size 2 bytes
# w                Represents unicode character of size 4 bytes
# l                Represents signed integer of size 4 bytes
# L                Represents unsigned integer of size 4 bytes
# f                Represents floating point of size 4 bytes
# d                Represents floating point of size 8 bytes

# * Arrays" in Python are not the arrays in conventional programming languages like C and Java, but closer to lists. A list can be a collection of either homogeneous or heterogeneous elements, and may contain ints, strings or other lists.

from array import *

my_array = array('i', [1, 2, 3, 4, 5])
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
# 1

# * An array is a data structure that stores values of same data type. In Python, this is the main difference between arrays and lists.

# * While python lists can contain values corresponding to different data types, arrays in python can only contain values corresponding to same data type. In this tutorial, we will understand the Python arrays with few examples

# * To use arrays in python language, you need to import the standard array module. This is because array is not a fundamental data type like strings, integer etc.

# ^ arrayIdentifierName = array(typeCode, [Initializers])

# * In the declaration above, arrayIdentifierName is the name of array, typeCode lets python know the type of array and Initializers are the values with which array is initialized.

# * TypeCodes are the codes that are used to define the type of array values or the type of array. The table above shows the possible values you can use when declaring an array and it's type.

my_array = array('i', [1, 2, 3, 4, 5])
for i in my_array:
    print(i)
