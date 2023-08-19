from collections import ChainMap
from itertools import chain

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

merged = {**fish, **dog}
print(merged)

# * As this example demonstrates, duplicate keys map to their lattermost value (for example "Clifford" overrides "Nemo")

merged2 = dict(ChainMap(fish, dog))
print(merged2)

# * With this technique the foremost value takes precedence for a given key rather than the last ("Clifford" is thrown out in favor of "Nemo").

merged3 = dict(chain(fish.items(), dog.items()))
print(merged3)

# * This uses the lattermost value, as with the **-based technique for merging ("Clifford" overrides "Nemo").

print(fish)
fish.update(dog)
print(fish)
# * dict.update uses the latter dict to overwrite the previous one.

print(merged == fish)  # True
print(merged2 == fish)  # False
print(merged3 == fish)  # True
