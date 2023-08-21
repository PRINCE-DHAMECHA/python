
# ~ Decorators augment the behavior of other functions or methods. Any function that takes a function as a parameter and returns an augmented function can be used as a decorator.

# * This simplest decorator does nothing to the function being decorated. Such
# * minimal decorators can occasionally be used as a kind of code markers.

def super_secret_function(f):
    return f


@super_secret_function
def my_function():
    print("This is my secret function.")

# * The @-notation is syntactic sugar that is equivalent to the following:


my_function = super_secret_function(my_function)

# * It is important to bear this in mind in order to understand how the decorators work. This "unsugared" syntax makes it clear why the decorator function takes a function as an argument, and why it should return another function. It also demonstrates what would happen if you don't return a function:


def disabled(f):
    """
    This function returns nothing, and hence removes the decorated function
    from the local scope.
    """
    pass


@disabled
def my_function():
    print("This function can no longer be called...")


# my_function()
# ! TypeError: 'NoneType' object is not callable


# * Thus, we usually define a new function inside the decorator and return it. This new function would first do something that it needs to do, then call the original function, and finally process the return value. Consider this simple decorator function that prints the arguments that the original function receives, then calls it.

# This is the decorator
def print_args(func):
    def inner_func(*args):
        print(args)
        # Call the original function with its arguments.
        return func(*args)
    return inner_func


@print_args
def multiply(num_a, num_b):
    return num_a * num_b


print(multiply(3, 5))
