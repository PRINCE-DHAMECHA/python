
# ~ Inserting {1,1,2,3} into set will be loss in fact that 1 occurs twice

from multiset import Multiset
from collections import Counter

listA = [1, 1, 1, 2, 2, 3]
counterA = Counter(listA)
print(counterA)

# * Counter is a dictionary where where elements are stored as dictionary keys and their counts are stored as dictionary values. And as all dictionaries, it is an unordered collection.

# ~ Multiset package is similar to the Python set but it allows elements to occur multiple times. Implementation can be based on dictionary elements( It internally uses a dict for storage) to their multiplicity in the multisets.

# print empty multiset
print(Multiset())

# print multiset from iterable
print(Multiset('abcde'))

# print multiset from mapping
m = Multiset({'a': 4, 'b': 2, 'c': 3, 'd': 1})
print(m)
print(type(m))
print(set(m))
