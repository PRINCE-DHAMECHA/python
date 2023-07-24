import keyword

# * <variable name> = <value>

# * Even though there's no need to specify a data type when declaring a variable in Python, while allocating the necessary area in memory for the variable, the Python interpreter automatically picks the most suitable built-in type for it:

a = 2
print(a)
print()

# ^Integer
b = 432423423423423423423
print(b)
print(type(b))

# ^Float
pi = 3.14
print(pi)
print(type(pi))

# ^String
c = 'Abc'
print(c)
print(type(c))
c = 'A'
print(c)
print(type(c))

# ^Boolean
b = True
print(b)
print(type(b))

# ^Null or Empty value
n = None
print(n)
print(type(n))
print()

# !Error
# 0 = x (Works from left to right not right to left :)

# * You can not use python's keywords as a valid variable name. You can see the list of keyword by:
print(keyword.kwlist)
# True = 2  # ! Error

# * Rules for variable naming:

# 1. Variables names must start with a letter or an underscore
# 2. The remainder of your variable name may consist of letters, numbers and underscores.

# * When you use = to do an assignment operation, what's on the left of = is a name for the object on the right. Finally, what = does is assign the reference of the object on the right to the name on the left.

a_name = 'an_object'  # "a_name" is now a name for the reference to the object "an_object"

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

#! Error
# x, y, z = 1, 2
# x, y = 1, 2, 3

p = q = r = 1
print(p, q, r)

# * Changing object
p = q = [1, 2, 3]
p = [2, 3]
print(p)
# ~ Q will still point to list that is first assigned, but p will refer to new list
print(q)

# ~ Modifying object but not changing object
p = q = [1, 2, 3]
p.append(4)
print(p)
print(q)

# * Variable type can be change for same variable

a = 5
print(a, type(a))
a = 'a'
print(a, type(a))

# ? If this bothers you, think about the fact that what's on the left of = is just a name for an object. First you call the int object with value 5, then you change your mind and decide to give the name a to a string object, having value 'New value'. Simple, right?
