
# * You can create an ordered dictionary which will follow a determined order when iterating over the keys in the dictionary.

# * Use OrderedDict from the collections module. This will always return the dictionary elements in the original insertion order when iterated over

from collections import OrderedDict
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 30
d['last'] = 29

# Outputs "first 1", "second 2", "third 3", "last 4"
for key in d:
    print(key, d[key])
