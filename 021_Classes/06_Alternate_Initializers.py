
# * Class methods present alternate ways to build instances of classes. To illustrate, let's look at an example.

# * Let's suppose we have a relatively simple Person class:

class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

# * It might be handy to have a way to build instances of this class specifying a full name instead of first and last name separately. One way to do this would be to have last_name be an optional parameter, and assuming that if it isn't given, we passed the full name in:


class Person(object):
    def __init__(self, first_name, age, last_name=None):
        if last_name is None:
            self.first_name, self.last_name = first_name.split(" ", 2)
        else:
            self.first_name = first_name
            self.last_name = last_name

        self.full_name = self.first_name + " " + self.last_name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

# ~ However, there are two main problems with this bit of code:

# * 1. The parameters first_name and last_name are now misleading, since you can enter a full name for first_name. Also, if there are more cases and/or more parameters that have this kind of flexibility, the if/elif/else branching can get annoying fast.

# * 2. Not quite as important, but still worth pointing out: what if last_name is None, but first_name doesn't split into two or more things via spaces? We have yet another layer of input validation and/or exception handling...

# * Enter class methods. Rather than having a single initializer, we will create a separate initializer, called from_full_name, and decorate it with the (built-in) classmethod decorator.


class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

# * Notice cls instead of self as the first argument to from_full_name. Class methods are applied to the overall class, not an instance of a given class (which is what self usually denotes). So, if cls is our Person class, then the returned value from the from_full_name class method is Person (first_name, last_name, age), which uses Person's __init__ to create an instance of the Person class. In particular, if we were to make a subclass Employee of Person, then from_full_name would work in the Employee class as well.


bob = Person("Bob", "Bobberson", 42)
bob2 = Person.from_full_name("Bob berson2", 31)

(bob.greet())
(bob2.greet())
