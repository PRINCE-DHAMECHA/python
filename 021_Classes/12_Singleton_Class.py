
# * Possibly the simplest design pattern is the singleton, which is a way to provide one and only one object of a particular type. To accomplish this, you must take control of object creation out of the hands of the programmer.

class SingleTone(object):
    __instance = None

    def __new__(cls, val):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
            # SingleTone.__instance = SingleTone(10)  # ! RecursionError: maximum recursion depth exceeded
        SingleTone.__instance.val = val
        return SingleTone.__instance


instance1 = SingleTone(10)
print(instance1.val)  # Output: 10

instance2 = SingleTone(20)
print(instance1.val)  # Output: 20
print(instance2.val)  # Output: 20

# Both instances are actually the same instance
print(instance1 == instance2)  # Output: True
print(instance1 is instance2)  # Output: True


class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Single:
    def __init__(self):
        self.name = None
        self.val = 0

    def getName(self):
        print(self.name)


x = Single.Instance()
y = Single.Instance()
x.name = 'I\'m single'
x.getName()  # outputs I'm single
y.getName()  # outputs I'm single
