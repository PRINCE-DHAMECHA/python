
# * You can use all() to determine if all the values in an iterable evaluate to True
nums = [1, 1, 0, 1]
all(nums)
# False
chars = ['a', 'b', 'c', 'd']
all(chars)
# True

# * Likewise, any() determines if one or more values in an iterable evaluate to True
nums = [1, 1, 0, 1]
any(nums)
# True
vals = [None, None, None, False]
any(vals)
# False

# * While this example uses a list, it is important to note these built-ins work with any iterable, including generators.

vals = [1, 2, 3, 4]
any(val > 12 for val in vals)
# False
any((val * 2) > 6 for val in vals)
# True
