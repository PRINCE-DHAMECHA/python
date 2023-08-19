
# * Packing
a = (1, 2, 3)  # a is the tuple (1, 2, 3)
# * Unpacking
x, y, z = a
print(a)
print(x)
print(y)
print(z)

# * The symbol _ can be used as a disposable variable name if one only needs some elements of a tuple, acting as a placeholder:

a = 1, 2, 3, 4
_, x, y, _ = a
# x == 2
# y == 3

first, *more, last = (1, 2, 3, 4, 5)
print(first, more, last)
# first == 1
# more == [2, 3, 4]
# last == 5
