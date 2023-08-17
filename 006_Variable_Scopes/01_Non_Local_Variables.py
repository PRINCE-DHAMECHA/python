
# ~ Python 3 added a new keyword called nonlocal. The nonlocal keyword adds a scope override to the inner scope. This is best illustrated with a couple of code examples. One of the most common examples is to create function that can increment:

def counter():
    num = 0

    def increment():
        num += 1
        return num
    return increment


x = counter()
# print(x())

# ! If you try running this code, you will receive an UnboundLocalError because the num variable is referenced before it is assigned in the innermost function. Let's add nonlocal to the mix:


def counter():
    num = 0

    def increment():
        nonlocal num
        num += 1
        return num
    return increment


x = counter()
print(x())
print(x())
print(x())
print(x())

# * Basically nonlocal will allow you to assign to variables in an outer scope, but not a global scope. So you can't use nonlocal in our counter function because then it would try to assign to a global scope. Give it a try and you will quickly get a SyntaxError. Instead you must use nonlocal in a nested function.

num = 0


def counter():

    def increment():
        # nonlocal num #! Error (Syntax)
        # num += 1  #! Error (UnboundLocalError)
        return num
    return increment


x = counter()
print(x())
print(x())
print(x())
print(x())
