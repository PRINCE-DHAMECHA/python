
# * If the variable contains a value of an immutable type (e.g. a string) then it is okay to assign a default value like this

class Rectangle(object):
    def __init__(self, width, height, color='blue'):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        return self.width * self.height


# Create some instances of the class
default_rectangle = Rectangle(2, 3)
print(default_rectangle.color)  # blue
red_rectangle = Rectangle(2, 3, 'red')
print(red_rectangle.color)  # red

# * One needs to be careful when initializing mutable objects such as lists in the constructor.


class Rectangle2D(object):
    def __init__(self, width, height, pos=[0, 0], color='blue'):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color


r1 = Rectangle2D(5, 3)
r2 = Rectangle2D(7, 8)
r1.pos[0] = 4
print(r1.pos)  # [4, 0]
print(r2.pos)  # [4, 0] r2's pos has changed as well

# * This behavior is caused by the fact that in Python default parameters are bound at function execution and not at function declaration. To get a default instance variable that's not shared among instances, one should use a construct like this:


class Rectangle2D(object):
    def __init__(self, width, height, pos=None, color='blue'):
        self.width = width
        self.height = height
        self.pos = pos or [0, 0]  # default value is [0, 0]
        self.color = color


r1 = Rectangle2D(5, 3)
r2 = Rectangle2D(7, 8)
r1.pos[0] = 4
print(r1.pos)  # [4, 0]
print(r2.pos)  # [0, 0] r2's pos hasn't changed
