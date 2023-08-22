
# * Python offers itself not only as a popular scripting language, but also supports the object-oriented programming paradigm. Classes describe data and provide methods to manipulate that data, all encompassed under a single object. Furthermore, classes allow for abstraction by separating concrete implementation details from abstract representations of data.

# * A class, functions as a template that defines the basic characteristics of a particular object. Here's an example:

class Person(object):
    """A simple class."""  # docstring
    species = "Homo Sapiens"  # class attribute

    def __init__(self, name):  # special method
        """This is the initializer. It's a special
        method (see below).
        """
        self.name = name  # instance attribute

    def __str__(self):  # special method
        """This method is run when Python tries
        to cast the object to a string. Return
        this string when using print(), etc.
        """
        return self.name

    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))

# ~ There are a few things to note when looking at the above example.

# * 1. The class is made up of attributes (data) and methods (functions).

# * 2. Attributes and methods are simply defined as normal variables and functions.

# * 3. As noted in the corresponding docstring, the __init__() method is called the initializer. It's equivalent to the constructor in other object oriented languages, and is the method that is first run when you create a new object, or new instance of the class.

# * 4. Attributes that apply to the whole class are defined first, and are called class attributes.

# * 5. Attributes that apply to a specific instance of a class (an object) are called instance attributes. They are generally defined inside __init__(); this is not necessary, but it is recommended (since attributes defined outside of __init__() run the risk of being accessed before they are defined).

# * 6. Every method, included in the class definition passes the object in question as its first parameter. The word self is used for this parameter (usage of self is actually by convention, as the word self has no inherent meaning in Python, but this is one of Python's most respected conventions, and you should always follow it).

# * 7. Those used to object-oriented programming in other languages may be surprised by a few things. One is that Python has no real concept of private elements, so everything, by default, imitates the behavior of the C++/Java public keyword.

# * 8. Some of the class's methods have the following form: __functionname__(self, other_stuff). All such methods are called "magic methods" and are an important part of classes in Python. For instance, operator overloading in Python is implemented with magic methods.

# ^ Now let's make a few instances of our Person class!


kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

# * We currently have three Person objects, kelly, joseph, and john_doe.
# * We can access the attributes of the class from each instance using the dot operator . Note again the difference between class and instance attributes:

# * Attributes
print(kelly.species)
# 'Homo Sapiens'
print(john_doe.species)
# 'Homo Sapiens'
print(joseph.species)
# 'Homo Sapiens'
print(kelly.name)
# 'Kelly'
print(joseph.name)
# 'Joseph'

# Methods
print(john_doe.__str__())
# 'John Doe'
print(john_doe)
# 'John Doe'
john_doe.rename("John")
# 'Now my name is John'
