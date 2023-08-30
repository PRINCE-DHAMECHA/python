
# * The dir() function can be used to get a list of the members of a class:

print(dir(list))

# * It is common to look only for "non-magic" members :-

for m in dir(list):
    if not m.startswith('__'):
        print(m)

# ! Classes can define a __dir__() method. If that method exists calling dir() will call __dir__(), otherwise Python will try to create a list of members of the class. This means that the dir function can have unexpected results. Two quotes of importance from the official python documentation:

# * If the object does not provide dir(), the function tries its best to gather information from the object’s dict attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be inaccurate when the object has a custom getattr().

# * Because dir() is supplied primarily as a convenience for use at an interactive prompt, it tries to supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names, and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the argument is a class.
