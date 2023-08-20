
# * There is a problem when using optional arguments with a mutable default type (described in Defining a function with optional arguments), which can potentially lead to unexpected behavior.

# * This problem arises because a function's default arguments are initialized once, at the point when the function is defined, and not (like many other languages) when the function is called. The default values are stored inside the function object's __defaults__ member variable.

def f(a, b=42, c=[]):
    pass


print(f.__defaults__)
# Out: (42, [])

# * For immutable types (see Argument passing and mutability) this is not a problem because there is no way to mutate the variable; it can only ever be reassigned, leaving the original value unchanged. Hence, subsequent are guaranteed to have the same default value. However, for a mutable type, the original value can mutate, by making calls to its various member functions. Therefore, successive calls to the function are not guaranteed to have the initial default value.


def append(elem, to=[]):
    to.append(elem)  # This call to append() mutates the default variable "to"
    return to


print(append(1))
# Out: [1]
print(append(2))  # Appends it to the internally stored list
# Out: [1, 2]
print(append(3, []))  # Using a new created list gives the expected result
# Out: [3]
# Calling it again without argument will append to the internally stored list again
print(append(4))
# Out: [1, 2, 4]

# * A common idiom to achieve this when a mutable type is needed as the default, is to use None (immutable) as the default argument and then assign the actual default value to the argument variable if it is equal to None.


def append(elem, to=None):
    if to is None:
        to = []
    to.append(elem)
    return to
