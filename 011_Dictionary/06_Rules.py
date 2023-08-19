
# * Every key must be unique (otherwise it will be overridden)
# * Every key must be hashable (can use the hash function to hash it; otherwise TypeError will be thrown)
# * There is no particular order for the key

# Creating and populating it with values
stock = {'eggs': 5, 'milk': 2}

# Or creating an empty dictionary
dictionary = {}
# And populating it after
dictionary['eggs'] = 5
dictionary['milk'] = 2

# Values can also be lists
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}

# Use list.append() method to add new elements to the values list
mydict['a'].append(4)  # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three']}

mydict['b'].append('four')
# => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three', 'four']}

# We can also create a dictionary using a list of two-items tuples
iterables = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterables)
print(dictionary)

# Or using keyword argument:
dictionary = dict(eggs=5, milk=2)
print(dictionary)

# Another way will be to use the dict.fromkeys:
dictionary = dict.fromkeys(('milk', 'eggs'))  # => {'milk': None, 'eggs': None}

dictionary = dict.fromkeys(('milk', 'eggs'), (2, 5))
# => {'milk': 2, 'eggs': 5}
