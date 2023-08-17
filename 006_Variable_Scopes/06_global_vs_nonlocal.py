
# ~ Both these keywords are used to gain write access to variables which are not local to the current functions

# The global keyword declares that a name should be treated as a global variable.

foo = 0  # global foo


def f1():
    foo = 1  # a new foo local in f1

    def f2():
        foo = 2  # a new foo local in f2

    def f3():
        foo = 3  # a new foo local in f3
        print(foo)  # 3
        foo = 30  # modifies local foo in f3 only

    def f4():
        global foo
        print(foo)  # 0
        foo = 100  # modifies global foo

# On the other hand, nonlocal (see Nonlocal Variables ), available in Python 3, takes a local variable from an enclosing scope into the local scope of current function.

# The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals.


def f1():

    def f2():
        foo = 2  # a new foo local in f2

        def f3():
            nonlocal foo  # foo from f2, which is the nearest enclosing scope
            print(foo)  # 2
            foo = 20  # modifies foo from f2!
        f3()
        print(foo)
    f2()


f1()
