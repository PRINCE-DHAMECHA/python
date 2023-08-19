myDict = {
    'a': '1',
    'b': '2'
}

print(myDict.keys())

print(myDict.values())

print(myDict.items())

# * NOTE: Because a dict is unsorted, keys(), values(), and items() have no sort order. Use sort(), sorted(), or an OrderedDict if you care about the order that these methods return.

# * Python 2/3 Difference: In Python 3, these methods return special iterable objects, not lists, and are the equivalent of the Python 2 iterkeys(), itervalues(), and iteritems() methods. These objects can be used like lists for the most part, though there are some differences. See PEP 3106 for more details.

print(myDict['a'])
