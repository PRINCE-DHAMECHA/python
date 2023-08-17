
# ~ What are local and global scope?

# * All Python variables which are accessible at some point in code are either in local scope or in global scope.
# * The explanation is that local scope includes all variables defined in the current function and global scope includes variables defined outside of the current function.

foo = 1  # global


def func():
    bar = 2  # local
    print(foo)  # prints variable foo from global scope
    print(bar)  # prints variable bar from local scope


func()

foo = 1


def func():
    bar = 2
    print(globals().keys())  # prints all variable names in global scope
    print(locals().keys())  # prints all variable names in local scope


func()

# ~ What happens with name clashes?

foo = 1


def func():
    foo = 3  # creates a new variable foo in local scope, global foo is not affected
    print(foo)  # prints 3
    # global variable foo still exists, unchanged:
    print(globals()['foo'])  # prints 1
    print(locals()['foo'])  # prints 3


func()

foo = 1


def func():
    global foo
    foo = 2  # this modifies the global foo, rather than creating a local variable


func()
print(foo)

# ~ The scope is defined for the whole body of the function!
# * What it means is that a variable will never be global for a half of the function and local afterwards, or vice-versa.

foo = 1


def func():
    # This function has a local variable foo, because it is defined down below.
    # So, foo is local from this point. Global foo is hidden.
    # print(foo)  # ! raises UnboundLocalError, because local foo is not yet initialized
    foo = 7
    print(foo)


func()

foo = 1


def func():
    global foo
    print(foo)
    foo = 2
    print(foo)


func()
print(foo)  # 2

foo = 1


def func():
    # In this function, foo is a global variable from the beginning
    foo = 7  # global foo is modified
    print(foo)  # 7
    print(globals()['foo'])  # 7
    # global foo  # ! SyntaxError: name 'foo' is used prior to global declaration
    print(foo)


func()

# ~ There may be many levels of functions nested within functions, but within any one function there is only one local scope for that function and the global scope. There are no intermediate scopes

foo = 1


def f1():
    bar = 1

    def f2():
        baz = 2
        # here, foo is a global variable, baz is a local variable
        # bar is not in either scope
        print(locals().keys())  # ['baz']
        print('bar' in locals())  # False
        print('bar' in globals())  # False

    def f3():
        baz = 3
        # bar from f1 is referenced so it enters local scope of f3 (closure)
        print(bar)
        print(locals().keys())  # ['bar', 'baz']
        print('bar' in locals())  # True
        print('bar' in globals())  # False

    def f4():
        bar = 4  # a new local bar which hides bar from local scope of f1
        baz = 4
        print(bar)
        print(locals().keys())  # ['bar', 'baz']
        print('bar' in locals())  # True
        print('bar' in globals())  # False
    f2()
    f3()
    f4()


f1()
