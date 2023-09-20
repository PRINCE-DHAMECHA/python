
# ~ In Python, a metaclass is a class that defines the behavior of other classes, specifically how they are created and how they behave. Metaclasses are often referred to as "classes for classes" because they define the structure and behavior of classes themselves.

# ~ In Python, everything is an object: integers, strings, lists, even functions and classes themselves are objects. And every object is an instance of a class.

print(type(5))

# * Most classes in python are instances of type. type itself is also a class. Such classes whose instances are also classes are called metaclasses


# ~ Metaclasses allow you to deeply modify the behaviour of Python classes (in terms of how they're defined, instantiated, accessed, and more) by replacing the type metaclass that new classes use by default.

# ~ Here's a simple example of a metaclass that enforces a coding standard by making sure all class attribute names are in uppercase:


class UppercaseAttributesMeta(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {key.upper(): value for key, value in attrs.items()}
        return super(UppercaseAttributesMeta, cls).__new__(cls, name, bases, uppercase_attrs)


class MyClass(metaclass=UppercaseAttributesMeta):
    a = 1
    b = 2


print(MyClass.A)  # Output: 1
print(MyClass.B)  # Output: 2
# print(MyClass.a) # ! AttributeError: type object 'MyClass' has no attribute 'a'. Did you mean: 'A'?

# ~ Functionality in metaclasses can be changed so that whenever a class is built, a string is printed to standard output, or an exception is thrown. This metaclass will print the name of the class being built.


class VerboseMetaclass(type):
    def __new__(cls, class_name, class_parents, class_dict):
        print("Creating class ", class_name)
        new_class = super().__new__(cls, class_name, class_parents, class_dict)
        return new_class


class Spam(metaclass=VerboseMetaclass):
    def eggs(self):
        print("[insert example string here]")


s = Spam()
print(s.eggs())


# ~ You may have heard that everything in Python is an object. It is true, and all objects have a class:

print(type(1))


class Foo:
    pass


bar = Foo()

print(type(bar))  # Foo

# * Foo itself is an instance of type
print(type(Foo))  # type
print(type(type))  # type

# ~ So what is a metaclass? For now let's pretend it is just a fancy name for the class of a class.

# * Everything is an object in Python, so everything has a class
# * The class of a class is called a metaclass
# * The default metaclass is type, and by far it is the most common metaclass

# * But why should you know about metaclasses? Well, Python itself is quite "hackable", and the concept of metaclass is important if you are doing advanced stuff like meta-programming or if you want to control how your classes are initialized.
