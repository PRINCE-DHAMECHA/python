import operator  # contains 2 argument arithmetic functions
import operator

a, b = 1, 2

print(a+b)

# ~ In place operations which is more effective shortcut
a += b
print(a)
# -= decrement the variable in place
# += increment the variable in place
# *= multiply the variable in place
# /= divide the variable in place
# //= floor divide the variable in place # Python 3
# %= return the modulus of the variable in place
# **= raise to a power in place

a = operator.add(a, b)
print(a, b)

a, b = 1, 2

# * since a is not mutable, it'll not change the value of a, but it will not the case with lists, sets, and dicts as it's mutable
c = operator.iadd(a, b)
print(a, b, c)

listA = [1, 2, 3]
listB = [4, 5, 6]

operator.iadd(listA, listB)
print(listA)  # [1, 2, 3, 4, 5, 6]

# * Strings are immutable
str1 = "Prince"
str2 = "Dhamecha"
operator.iadd(str1, str2)
print(str1)

# ~ Subtraction

a, b = 1, 2
# Using the "-" operator:
b - a  # = 1
operator.sub(b, a)  # = 1

# int and int (gives an int)
# int and float (gives a float)
# int and complex (gives a complex)
# float and float (gives a float)
# float and complex (gives a complex)
# complex and complex (gives a complex)

# ~ Multiplication

a, b = 2, 3
a * b  # = 6
operator.mul(a, b)  # = 6

# int and int (gives an int)
# int and float (gives a float)
# int and complex (gives a complex)
# float and float (gives a float)
# float and complex (gives a complex)
# complex and complex (gives a complex)

# * Note: The * operator is also used for repeated concatenation of strings, lists, and tuples:

print(3 * 'ab')  # = 'ababab'
print(3 * ('a', 'b'))  # = ('a', 'b', 'a', 'b', 'a', 'b')

# ! Error
# print('abc' - 'bc')
