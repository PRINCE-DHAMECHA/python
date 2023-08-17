

# ~ If v is a variable, the command del v removes the variable from its scope. For example:

x = 5
print(x)  # out: 5
del x
# print(x)  # ! NameError: name 'x' is not defined

# * Note that del is a binding occurrence, which means that unless explicitly stated otherwise (using nonlocal or global), del v will make v local to the current scope. If you intend to delete v in an outer scope, use nonlocal v or global v in the same scope of the del v statement.
