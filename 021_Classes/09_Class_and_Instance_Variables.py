
# * Instance variables are unique for each instance, while class variables are shared by all instances.

class C:
    x = 2  # class variable

    def __init__(self, y):
        self.y = y  # instance variable


print(C.x)
# 2
# print(C.y)
# ! AttributeError: type object 'C' has no attribute 'y'
c1 = C(3)
print(c1.x)
# 2
print(c1.y)
# 3
c2 = C(4)
print(c2.x)
# 2
print(c2.y)
# 4

# * Class variables can be accessed on instances of this class, but assigning to the class attribute will create an instance variable which shadows the class variable

c2.x = 4
print(c2.x)
# 4
print(C.x)
# 2

# * Note that mutating class variables from instances can lead to some unexpected consequences.


class D:
    x = []

    def __init__(self, item):
        self.x.append(item)  # note that this is not an assignment!


d1 = D(1)
d2 = D(2)
print(d1.x)
# [1, 2]
print(d2.x)
# [1, 2]
print(D.x)
# [1, 2]
