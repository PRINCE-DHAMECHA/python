
# * Inheritance in Python is based on similar ideas used in other object oriented languages like Java, C++ etc. A new class can be derived from an existing class as follows.

class BaseClass(object):
    pass


class DerivedClass(BaseClass):
    pass

# * The BaseClass is the already existing (parent) class, and the DerivedClass is the new (child) class that inherits (or subclasses) attributes from BaseClass. Note: As of Python 2.2, all classes implicitly inherit from the object class, which is the base class for all built-in types.

# * We define a parent Rectangle class in the example below, which implicitly inherits from object:


class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# * The Rectangle class can be used as a base class for defining a Square class, as a square is a special case of rectangle.


class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s

# * The Square class will automatically inherit all attributes of the Rectangle class as well as the object class. supe () is used to call the __init__() method of Rectangle class, essentially calling any overridden method of the base class. Note: in Python 3, super() does not require arguments.

# * Derived class objects can access and modify the attributes of its base classes:


r = Rectangle(2, 3)
print(r.area())
# Output: 6
print(r.perimeter())
# Output: 10

s = Square(3)
print(s.area())
# Output: 9
print(s.perimeter())
# Output: 12

# ~ Built-in functions that work with inheritance

# * issubclass(DerivedClass, BaseClass): returns True if DerivedClass is a subclass of the BaseClass

# * isinstance(s, Class): returns True if s is an instance of Class or any of the derived classes of Class

# subclass check
print(issubclass(Square, Rectangle))
# Output: True

print(isinstance(r, Rectangle))
# Output: True
print(isinstance(r, Square))
# Output: False
# A rectangle is not a square

print(isinstance(s, Rectangle))
# Output: True
# A square is a rectangle
print(isinstance(s, Square))
# Output: True

# ~ Multiple Inheritance

# * Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes, including methods. This is known as the Method Resolution Order (MRO).


class Foo(object):
    foo = 'attr foo of Foo'


class Bar(object):
    foo = 'attr foo of Bar'  # we won't see this.
    bar = 'attr bar of Bar'


class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'


# * Now if we instantiate FooBar, if we look up the foo attribute, we see that Foo's attribute is found first
fb = FooBar()
print(fb.foo)  # First one takes priority
print(FooBar.mro())

# ~ It can be simply stated that Python's MRO algorithm is
# * 1. Depth first (e.g. FooBar then Foo) unless
# * 2. a shared parent (object) is blocked by a child (Bar) and
# * 3. no circular relationships allowed
# * That is, for example, Bar cannot inherit from FooBar while FooBar inherits from Bar.

# * Another powerful feature in inheritance is super. super can fetch parent classes features.


class Foo(object):
    def foo_method(self):
        print("foo Method")


class Bar(object):
    def bar_method(self):
        print("bar Method")


class FooBar(Foo, Bar):
    def foo_method(self):
        super(FooBar, self).foo_method()

# * Multiple inheritance with init method of class, when every class has own init method then we try for multiple inheritance then only init method get called of class which is inherit first.
# * for below example only Foo class init method getting called Bar class init not getting called


class Foo(object):
    def __init__(self):
        print("foo init")


class Bar(object):
    def __init__(self):
        print("bar init")


class FooBar(Foo, Bar):
    def __init__(self):
        print("foobar init")
        super(FooBar, self).__init__()


a = FooBar()
#  foobar init
#  foo init

# * But it doesn't mean that Bar class is not inherit. Instance of final FooBar class is also instance of Bar class and Foo class

print(isinstance(a, FooBar))
print(isinstance(a, Foo))
print(isinstance(a, Bar))
# True
# True
# True
