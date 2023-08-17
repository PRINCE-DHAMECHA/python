import operator

print(3 % 4)
print(3 % 2)
print(6 % 4)

print(operator.mod(10, 2))
print(operator.mod(10, 4))

print(-9 % 5)  # * 5 - (9 % 5)


# * If you need to find the result of integer division and modulus, you can use the divmod function as a shortcut:

quo, rem = divmod(9, 5)
print(type(divmod(6, 7)))
print(quo, rem)
