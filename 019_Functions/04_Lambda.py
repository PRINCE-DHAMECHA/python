
# * The lambda keyword creates an inline function that contains a single expression. The value of this expression is what the function returns when invoked.

# greet_me = lambda: "Hello"

# * This creates an inline function with the name greet_me that returns Hello. Note that you don't write return when creating a function with lambda. The value after : is automatically returned.

# print(greet_me())

# * lambdas can take arguments, too:

# strip_and_upper_case = lambda s: s.strip().upper()
# strip_and_upper_case(" Hello ")


# * They can also take arbitrary number of arguments / keyword arguments, like normal FunctionDef

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')
# hello ('world',) {'world': 'world'}

# ^ lambdas are commonly used for short functions that are convenient to define at the point where they are called (typically with sorted, filter and map).

# * For example, this line sorts a list of strings ignoring their case and ignoring whitespace at the beginning and at the end:

print(sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip().upper()))
# Out:
# [' bAR', 'BaZ ', ' foo ']

my_list = [3, -4, -2, 5, 1, 7]
print(sorted(my_list, key=lambda x: abs(x)))
print(my_list)
# Out:
# [1, -2, 3, -4, 5, 7]

# * Bear in mind that PEP-8 (the official Python style guide) does not recommend assigning lambdas to variables (as we did in the first two examples)


# Yes:
def f(x): return 2*x

# No:
# f = lambda x: 2*x

# The first form means that the name of the resulting function object is specifically f instead of the generic <lambda>. This is more useful for traceBacks and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression).
