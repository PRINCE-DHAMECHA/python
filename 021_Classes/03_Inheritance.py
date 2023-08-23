
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
