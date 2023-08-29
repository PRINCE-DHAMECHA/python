
# * Class composition allows explicit relations between objects. In this example, people live in cities that belong to countries. Composition allows people to access the number of all people living in their country:

class Country(object):
    def __init__(self):
        self.cities = []

    def addCity(self, city):
        self.cities.append(city)


class Person(object):
    def __init__(self, ID):
        self.ID = ID
        self.city = None

    def join_city(self, city):
        self.city = city
        city.addPerson(self)

    def people_in_my_country(self):
        x = sum([len(c.people) for c in self.city.country.cities])
        return x


class City(object):
    def __init__(self):
        self.people = []
        self.country = None

    def addPerson(self, person):
        self.people.append(person)
        person.city = self

    def join_country(self, country):
        self.country = country
        country.addCity(self)


IND = Country()

RJKT = City()

RJKT.addPerson(Person(2))
Person(1).join_city(RJKT)
RJKT.addPerson(Person(3))

RJKT.join_country(IND)
print(IND.cities[0].people[0].people_in_my_country())
# 3

JNGD = City()

JNGD.addPerson(Person(5))
JNGD.addPerson(Person(6))

RJKT.addPerson(Person(10))

JNGD.addPerson(Person(10))
JNGD.addPerson(Person(7))
JNGD.join_country(IND)

print(IND.cities[0].people[0].people_in_my_country())
# 8
