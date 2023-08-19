
# * A dictionary is an example of a key value store also known as Mapping in Python. It allows you to store and retrieve elements by referencing a key. As dictionaries are referenced by key, they have very fast lookups. As they are primarily used for referencing items by key, they are not sorted.

d = {}  # empty dict

d = {'key': 'value'}  # dict with initial values
print(d)

# Also unpacking one or multiple dictionaries with the literal syntax is possible=
d1 = {**d}

d1['key'] = 1
print(d)
print(d1)

d = {k: v for k, v in [('key1', 'value1',)]}
print(d)

d = dict()  # empty dict
d = dict(key2='value')  # explicit keyword arguments
print(d)
d = dict([('key', 'value')])  # passing in a list of key/value pairs
print(d)
# make a shallow copy of another dict (only possible if keys are only strings!)
d = dict(**d1)

# * modifying a dict
# To add items to a dictionary, simply create a new key with a value:
d['newkey'] = 42
print(d)

# * It also possible to add list and dictionary as value:
d['new_list'] = [1, 2, 3]
print(d)
d['new_dict'] = {'nested_dict': 1}
print(d)

# To delete an item, delete the key from the dictionary:
del d['newkey']
print(d)
