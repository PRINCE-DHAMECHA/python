
# * Closures in Python are created by function calls. Here, the call to makeInc creates a binding for x that is referenced inside the function inc. Each call to makeInc creates a new instance of this function, but each instance has a link to a different binding of x.

def makeInc(x):
    def inc(y):
        # x is "attached" in the definition of inc
        return y + x
    return inc


incOne = makeInc(1)
incFive = makeInc(5)
print(incOne(5))  # returns 6
print(incFive(5))  # returns 10

# Notice that while in a regular closure the enclosed function fully inherits all variables from its enclosing environment, in this construct the enclosed function has only read access to the inherited variables but cannot make assignments to them


# def makeInc(x):
#     def inc(y):
#         # incrementing x is not allowed
#         x += y
#         return x
#     return inc


# incOne = makeInc(1)
# incOne(5)  # ! UnboundLocalError: local variable 'x' referenced before assignment

# ~ All parameters specified after the first asterisk in the function signature are keyword-only.

def f(*a, b):
    pass


# f(1, 2, 3)
# ! TypeError: f() missing 1 required keyword-only argument: 'b'

# * In Python 3 it's possible to put a single asterisk in the function signature to ensure that the remaining arguments may only be passed using keyword arguments.

def f(a, b, *, c):
    pass


# f(1, 2, 3)
# TypeError: f() takes 2 positional arguments but 3 were given
f(1, 2, c=3)
# No error
