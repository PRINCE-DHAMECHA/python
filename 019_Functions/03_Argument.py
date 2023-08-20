
# * Defining a function capable of taking an arbitrary number of arguments can be done by prefixing one of the arguments with a *


# * args will be a tuple containing all values that are passed in
def func(*args):
    for i in args:
        print(i)


func(1, 2, 3)  # Calling it with 3 arguments

list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values)  # Calling it with list of values, * expands the list

func(*(1, 2, 3))
func(*[1, 2, 3])
func(*{1, 2, 3})
func()

# * You can't provide a default for args, for example func(*args=[1, 2, 3]) will raise a syntax error (won't even compile).

# * You can take an arbitrary number of arguments with a name by defining an argument in the definition with two * in front of it:


def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)


func(value1=1, value2=2, value3=3)  # Calling it with 3 arguments
# Out: value1 1
# value2 2
# value3 3
func()  # Calling it without arguments
# No Out put
my_dict = {'foo': 1, 'bar': 2}
my_dict2 = {'foo2': 1, 'bar2': 2}
func(**my_dict, **my_dict2)  # Calling it with a dictionary
# Out: foo 1
# bar 2

# ! You can't provide these without names, for example func(1, 2, 3) will raise a TypeError.
# func(1, 2, 2)

# * You can mix these with other optional and required arguments but the order inside the definition matters.

# The positional/keyword arguments come first. (Required arguments).
# Then comes the arbitrary *arg arguments. (Optional).
# Then keyword-only arguments come next. (Required).
# Finally the arbitrary keyword **kwargs come. (Optional).


def func(arg1, arg2=10, *args, kwarg1, kwarg2=2, **kwargs):
    pass

# * arg1 must be given, otherwise a TypeError is raised. It can be given as positional (func(10)) or keyword argument (func(arg1=10)).

# * kwarg1 must also be given, but it can only be provided as keyword-argument: func(kwarg1=10).

# * arg2 and kwarg2 are optional. If the value is to be changed the same rules as for arg1 (either positional or keyword) and kwarg1 (only keyword) apply.

# *args catches additional positional parameters. But note, that arg1 and arg2 must be provided as positional arguments to pass arguments to *args: func(1, 1, 1, 1).

# **kwargs catches all additional keyword parameters. In this case any parameter that is not arg1, arg2, kwarg1 or kwarg2. For example: func(kwarg3=10).

# * In Python 3, you can use * alone to indicate that all subsequent arguments must be specified as keywords.

# * For instance the math.isclose function in Python 3.5 and higher is defined using def math.isclose (a, b, *, rel_tol=1e-09, abs_tol=0.0), which means the first two arguments can be supplied positionally but the optional third and fourth parameters can only be supplied as keyword arguments.

# ~ Note on Naming

# * The convention of naming optional positional arguments args and optional keyword arguments kwargs is just a convention you can use any names you like but it is useful to follow the convention so that others know what you are doing, or even yourself later so please do.

# ~ Note on Uniqueness

# * Any function can be defined with none or one *args and none or one **kwargs but not with more than one of each. Also *args must be the last positional argument and **kwargs must be the last parameter. Attempting to use more than one of either will result in a Syntax Error exception.

# ~ Note on Nesting Functions with Optional Arguments

# * It is possible to nest such functions and the usual convention is to remove the items that the code has already handled but if you are passing down the parameters you need to pass optional positional args with a * prefix and optional keyword args with a ** prefix, otherwise args with be passed as a list or tuple and kwargs as a single dictionary. e.g.:


def fn(**kwargs):
    print(kwargs)
    f1(**kwargs)
    # f1(kwargs) #! TypeError
    # f1(*kwargs) #! TypeError


def f1(**kwargs):
    print(len(kwargs))


fn(a=1, b=2)
# Out:
# {'a': 1, 'b': 2}
# 2


# * Optional arguments can be defined by assigning (using =) a default value to the argument-name:

def make(action='nothing'):
    return action


# Calling this function is possible in 3 different ways:
make("fun")
# Out: fun
make(action="sleep")
# Out: sleep
# The argument is optional so the function will use the default value if the argument is
# not passed in.
make()
# Out: nothing


def func(lst):
    lst.append(2)


mylst = [1, 2, 3]
func(mylst)
print(mylst)  # [1, 2, 3, 4]

# * argument (actual parameter): the actual variable being passed to a function;

# * parameter (formal parameter): the receiving variable that is used in a function.

# * In Python, arguments are passed by assignment (as opposed to other languages, where arguments can be passed by value/reference/pointer).

# * Mutating a parameter will mutate the argument (if the argument's type is mutable).


def foo(x):  # here x is the parameter
    x[0] = 9  # This mutates the list labelled by both x and y
    print(x)


y = [4, 5, 6]
foo(y)  # call foo with y as argument
# Out: [9, 5, 6] # list labelled by x has been mutated
print(y)
# Out: [9, 5, 6] # list labelled by y has been mutated too

# * Reassigning the parameter won’t reassign the argument.


def foo(x):  # here x is the parameter, when we call foo(y) we assign y to x
    x[0] = 9  # This mutates the list labelled by both x and y
    x = [1, 2, 3]  # x is now labeling a different list (y is unaffected)
    x[2] = 8  # This mutates x's list, not y's list


y = [4, 5, 6]  # y is the argument, x is the parameter
foo(y)  # Pretend that we wrote "x = y", then go to line 1
print(y)
# Out: [9, 5, 6]

# * In Python, we don’t really assign values to variables, instead we bind (i.e. assign, attach) variables (considered as names) to objects.

# ^ Immutable: Integers, strings, tuples, and so on. All operations make copies.

# ^ Mutable: Lists, dictionaries, sets, and so on. Operations may or may not mutate.

x = [3, 1, 9]
y = x
# Mutates the list labelled by x and y, both x and y are bound to [3, 1, 9]
x.append(5)
x.sort()  # Mutates the list labelled by x and y (in-place sorting)
x = x + [4]  # Does not mutate the list (makes a copy for x only, not y)
z = x  # z is x ([1, 3, 9, 4])
# Mutates the list labelled by both x and z (uses the extend function).
x += [6]
x = sorted(x)  # Does not mutate the list (makes a copy for x only).
print(x)
# Out: [1, 3, 4, 5, 6, 9]
print(y)
# Out: [1, 3, 5, 9]
print(z)
# Out: [1, 3, 5, 9, 4, 6]


def unpacking(a, b, c=45, d=60, *args, **kwargs):
    print(a, b, c, d, args, kwargs)


unpacking(1, 2, 3, 4)
# 1 2 3 4 () {}
unpacking(1, 2)
# 1 2 45 60 () {}
unpacking(1, 2, d=3, c=4)
# 1 2 4 3 () {}

pair = (3, )
print(type(pair))
# Tuple
unpacking(1, 2, *pair, d=4)
# 1 2 3 4 () {}
unpacking(1, 2, d=4, *pair)
# 1 2 3 4 () {}
print(*pair)
# unpacking(1, 2,  *pair, c=4)
# unpacking(1, 2, c=4, *pair)
# ! TypeError: unpacking() got multiple values for argument 'c'
# We assigned c=4 but then again pair will assign 3

pair = (3, 4)
# unpacking(1, 2, *pair, d=4)
# ! TypeError: unpacking() got multiple values for argument 'd'
#  We assigned 4 to d using pair but then we again try to assign using d=4

arg_dict = {'c': 3, 'd': 4, 'not_a_parameter': 75}
unpacking(1, 2, **arg_dict)
# 1 2 3 4 () {'not_a_parameter': 75}

# unpacking(1, 2, *pair, **arg_dict)
# ! TypeError: unpacking() got multiple values for argument 'c'

arg_dict = {'d': 4, 'not_a_parameter': 75}
# unpacking(1, 2, *pair, **arg_dict)
# ! TypeError: unpacking() got multiple values for argument 'd'

# unpacking(1, 2, 3, c=4)
# ! TypeError: unpacking() got multiple values for argument 'c'
