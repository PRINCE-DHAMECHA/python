
# * Using the def statement is the most common way to define a function in python. This statement is a so called single clause compound statement with the following syntax:

# def function_name(parameters):
#  statement(s)

# * function_name is known as the identifier of the function. Since a function definition is an executable statement its execution binds the function name to the function object which can be called later on using the identifier.

# * parameters is an optional list of identifiers that get bound to the values supplied as arguments when the function is called. A function may have an arbitrary number of arguments which are separated by commas.

# * statement(s) - also known as the function body - are a nonempty sequence of statements executed each time the function is called. This means a function body cannot be empty, just like any indented block.

# * Here’s an example of a simple function definition which purpose is to print Hello each time it’s called:

def greet():
    print("Hello")


# Now let’s call the defined greet() function:

greet()
# Out: Hello


def greet_two(greeting):
    print(greeting)


greet_two("Howdy")
# Out: Howdy

# Also you can give a default value to that function argument


def greet_two(greeting="Howdy"):
    print(greeting)


greet_two()
# Out: Howdy

# * You'll notice that unlike many other languages, you do not need to explicitly declare a return type of the function. Python functions can return values of any type via the return keyword. One function can return any number of different types!


def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0


print(many_types(1))
print(many_types(-1))
# # Output:
# 0
# Hello!

# * A function that reaches the end of execution without a return statement will always return None:


def do_nothing():
    pass


print(do_nothing())
# Out: None

# * As mentioned previously a function definition must have a function body, a nonempty sequence of statements. Therefore the pass statement is used as function body, which is a null operation – when it is executed, nothing happens. It does what it means, it skips. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed.
