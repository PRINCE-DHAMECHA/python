
# * Python classes support properties, which look like regular object variables, but with the possibility of attaching custom behavior and documentation

class MyClass(object):
    def __init__(self):
        self._my_string = ""

    @property
    def string(self):
        print("Getter Called")
        """A profoundly important string."""
        return self._my_string

    @string.setter
    def string(self, new_value):
        print("Setter Called")
        assert isinstance(new_value, str), \
            "Give me a string, not a %r!" % type(new_value)
        self._my_string = new_value

    @string.deleter
    def string(self):
        print("Deleter Called")
        self._my_string = None

# * The object's of class MyClass will appear to have a property .string, however it's behavior is now tightly controlled:


mc = MyClass()
mc.string = "String!"
print(mc.string)
del mc.string
# mc.x
print(mc.string)

# * As well as the useful syntax as above, the property syntax allows for validation, or other augmentations to be added to those attributes. This could be especially useful with public APIs - where a level of help should be given to the user

# * Another common use of properties is to enable the class to present 'virtual attributes' - attributes which aren't actually stored but are computed only when requested.


class Character(object):
    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self.max_hp = max_hp

    # Make hp read only by not providing a set method
    @property
    def hp(self):
        return self._hp

    # Make name read only by not providing a set method
    @property
    def name(self):
        return self.name

    def take_damage(self, damage):
        self._hp -= damage
        self._hp = 0 if self.hp < 0 else self.hp

    @property
    def is_alive(self):
        return self.hp != 0

    @property
    def is_wounded(self):
        return self.hp < self.max_hp if self.hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive


bilbo = Character('Bilbo Baggins', 100)
print(bilbo.hp)
# out : 100
# bilbo.hp = 200
# ! out : AttributeError: can't set attribute hp attribute is read only.
print(bilbo.is_alive)
# out : True
print(bilbo.is_wounded)
# out : False
print(bilbo.is_dead)
# out : False
bilbo.take_damage(50)
print(bilbo.hp)
# out : 50
print(bilbo.is_alive)
# out : True
print(bilbo.is_wounded)
# out : True
print(bilbo.is_dead)
# out : False
bilbo.take_damage(50)
print(bilbo.hp)
# out : 0
print(bilbo.is_alive)
# out : False
print(bilbo.is_wounded)
# out : False
print(bilbo.is_dead)
# out : True
