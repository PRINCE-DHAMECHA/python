
# * New-style classes were introduced in Python 2.2 to unify classes and types. They inherit from the top-level object type. A new-style class is a user-defined type, and is very similar to built-in typ

# new-style class
class New(object):
    pass


# new-style instance
new = New()
print(new.__class__)
# <class '__main__.New'>
print(type(new))
# <class '__main__.New'>
print(issubclass(New, object))
# True

# * Old-style classes do not inherit from object. Old-style instances are always implemented with a built-in instance type.

# old-style class


# class Old:
#     pass
# # old-style instance
# old = Old()
# print(old.__class__)
# # <class __main__.Old at ...>
# print(type(old))
# # <type 'instance'>
# print(issubclass(Old, object))
# # False

# * New-style classes in Python 3 implicitly inherit from object, so there is no need to specify MyClass(object) anymore.

class MyClass:
    pass


my_inst = MyClass()
print(type(my_inst))
# <class '__main__.MyClass'>
print(my_inst.__class__)
# <class '__main__.MyClass'>
print(issubclass(MyClass, object))
# True
