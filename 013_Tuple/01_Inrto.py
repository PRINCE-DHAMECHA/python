
# ~ A tuple is an immutable list of values. Tuples are one of Python's simplest and most common collection types, and can be created with the comma operator (value = 1, 2, 3).


# * Syntactically, a tuple is a comma-separated list of values:
t = 'a', 'b', 'c', 'd', 'e'

# * Although not necessary, it is common to enclose tuples in parentheses:
t = ('a', 'b', 'c', 'd', 'e')

# * Create an empty tuple with parentheses:
t0 = ()
type(t0)  # <type 'tuple'>

# * To create a tuple with a single element, you have to include a final comma:
t1 = 'a',
type(t1)  # <type 'tuple'>

# * Note that a single value in parentheses is not a tuple:
t2 = ('a')
type(t2)  # <type 'str'>

# * To create a singleton tuple it is necessary to have a trailing comma.
t2 = ('a',)
type(t2)  # <type 'tuple'>

# * Note that for singleton tuples it's recommended (see PEP8 on trailing commas) to use parentheses. Also, no white space after the trailing comma (see PEP8 on whitespaces)

t2 = ('a',)  # PEP8-compliant
t2 = 'a',  # this notation is not recommended by PEP8
t2 = ('a', )  # this notation is not recommended by PEP8

# * Another way to create a tuple is the built-in function tuple.

t = tuple('lupins')
print(t)  # ('l', 'u', 'p', 'i', 'n', 's')
t = tuple(range(3))
print(t)  # (0, 1, 2)
