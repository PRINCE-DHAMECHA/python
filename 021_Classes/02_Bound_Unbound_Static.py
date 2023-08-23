
# * The idea of bound and unbound methods was removed in Python 3. In Python 3 when you declare a method within a class, you are using a def keyword, thus creating a function object. This is a regular function, and the surrounding class works as its namespace. In the following example we declare method f within class A, and it becomes a function A.f:

import inspect


class A(object):
    def f(self, x):
        print("Inside Function")
        print(self)
        print("x", x)
        return 2 * x


print(A.f)
# <function A.f at ...> (in Python 3.x)

# * In Python 2 the behavior was different: function objects within the class were implicitly replaced with objects of type instancemethod, which were called unbound methods because they were not bound to any particular class instance. It was possible to access the underlying function using .__func__ property.

# A.f
# # <unbound method A.f> (in Python 2.x)
# A.f.__class__
# # <type 'instancemethod'>
# A.f.__func__
# # <function f at ...>

# * The latter behaviors are confirmed by inspection - methods are recognized as functions in Python 3, while the distinction is upheld in Python 2.

# Python 3.x Version ≥ 3.0
print(inspect.isfunction(A.f))
# True
print(inspect.ismethod(A.f))
# False

# Python 2.x Version ≥ 2.3
# import inspect
# inspect.isfunction(A.f)
# # False
# inspect.ismethod(A.f)
# # True

# * In both versions of Python function/method A.f can be called directly, provided that you pass an instance of class A as the first argument.

print(A.f(1, 7))
# Python 2: TypeError: unbound method f() must be called with
# A instance as first argument (got int instance instead)
# Python 3:
# Inside Function
# 1
# x 7
# 14

a = A()
print(A.f(a, 20))
# Python 2 & 3:
# Inside Function
# <__main__.A object at 0x000002489C3FBF40>
# x 20
# 40

# * Now suppose a is an instance of class A, what is a.f then? Well, intuitively this should be the same method f of class A, only it should somehow "know" that it was applied to the object a – in Python this is called method bound to a.

# * The nitty-gritty details are as follows: writing a.f invokes the magic __getattribute__ method of a, which first checks whether a has an attribute named f (it doesn't), then checks the class A whether it contains a method with such a name (it does), and creates a new object m of type method which has the reference to the original A.f in m.__func__, and a reference to the object a in m.__self__. When this object is called as a function, it simply does the following: m(...) => m.__func__(m __self__, ...). Thus this object is called a bound method because when invoked it knows to supply the object it was bound to as the first argument. (These things work same way in Python 2 and 3)

print(a.f(2))

a = A()
print(a.f)
# <bound method A.f of <__main__.A object at ...>>
print(a.f(2))
# 4
# Note: the bound method object a.f is recreated *every time* you call it:
print(a.f is a.f)  # False
# As a performance optimization you can store the bound method in the object's
# __dict__, in which case the method object will remain fixed:
a.f = a.f
print(a.f is a.f)
# True

# * Finally, Python has class methods and static methods – special kinds of methods. Class methods work the same way as regular methods, except that when invoked on an object they bind to the class of the object instead of to the object. Thus m.__self__ = type(a). When you call such bound method, it passes the class of a as the first argument. Static methods are even simpler: they don't bind anything at all, and simply return the underlying function without any transformations.


class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)


print(D.f)
# <bound method type.f of <class '__main__.D'>>
print(D.f(12))
# 24
print(D.g)
# <function D.g at ...>
D.g("Mom")
# Hello, Mom

# * Note that class methods are bound to the class even when accessed on the instance:

d = D()
d.multiplier = 1337
print((D.multiplier, d.multiplier))
# (2, 1337)
print(d.f)
# <bound method D.f of <class '__main__.D'>>
print(d.f(10))
# 20

# * It is worth noting that at the lowest level, functions, methods, staticmethods, etc. are actually descriptors that invoke __get__, __set__ and optionally __del__ special methods
