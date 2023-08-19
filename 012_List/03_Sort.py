import datetime
from operator import itemgetter, attrgetter

# ~ sort()

a = [1, 2, 3, 4, 5, 7, 6, 8]

a.sort()

# * Lists can also be reversed when sorted using the reverse=True flag in the sort() method.

a.sort(reverse=True)
# a = [8, 7, 6, 5, 4, 3, 2, 1]

# * Lists can also be sorted using attrgetter and itemgetter functions from the operator module. These can help improve readability and reusability. Here are some examples:

people = [{'name': 'chandan', 'age': 20, 'salary': 2000},
          {'name': 'chetan', 'age': 18, 'salary': 5000},
          {'name': 'guru', 'age': 30, 'salary': 3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age)  # in-place sorting by age
print(people)
people.sort(key=by_salary, reverse=True)  # in-place sorting by salary
print(people)

# * itemgetter can also be given an index. This is helpful if you want to sort based on indices of a tuple.

list_of_tuples = [(1, 2), (3, 4), (5, 0)]
list_of_tuples.sort(key=itemgetter(1))
print(list_of_tuples)  # [(5, 0), (1, 2), (3, 4)]

# * Use the attrgetter if you want to sort by attributes of an object,


class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
           Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]  # reusing Person class from above example
persons.sort(key=attrgetter('name'))  # sort by name
print(persons)
by_birthday = attrgetter('birthday')
persons.sort(key=by_birthday)  # sort by birthday
print(persons)
