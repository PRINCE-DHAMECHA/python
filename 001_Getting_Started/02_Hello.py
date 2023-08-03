print('Hello Mom!!')

# ^ Run:- python 02_Hello.py

# * Interactive Prompt:-
# ^ python -i 02_Hello.py (quit() or exit() to close)

# * Argument as a program:-
# ^ python -c "print('Hello Mom')"


# ~ Comments

# ^ (I) Single line comment

"""
multiline
"""

# ~ docstrings


def func():
    """This is a function that does nothing at all"""
    return


print(func.__doc__)
help(func)


def greet(name, greeting="Hello"):
    """Print a greeting to the user `name`
    Optional parameter `greeting` can change what they're greeted with."""

    print("{} {}".format(greeting, name))


help(greet)


# ! Just putting no docstring or a regular comment in a function makes it a lot less helpful.


def greet(name, greeting="Hello"):
    # Print a greeting to the user `name`
    # Optional parameter `greeting` can change what they're greeted with.

    print("{} {}".format(greeting, name))


print(greet.__doc__)

help(greet)
