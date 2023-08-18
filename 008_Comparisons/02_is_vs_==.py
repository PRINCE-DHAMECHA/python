
# * a == b compares the value of a and b.
# * a is b will compare the identities of a and b.

a = 'Python is fun!'
b = 'Python is fun!'
print(a == b)  # returns True
print(a is b)  # returns True
a = [1, 2, 3, 4, 5]
b = a  # b references a
print(a == b)  # True
print(a is b)  # True
b = a[:]  # b now references a copy of a
print(a == b)  # True
print(a is b)  # False [!!]

# * Basically, is can be thought of as shorthand for id(a) == id(b).

# You should use is to test for None:

myvar = None

if myvar is not None:
    print("not None")
    pass

if myvar is None:
    print("None")
    pass
