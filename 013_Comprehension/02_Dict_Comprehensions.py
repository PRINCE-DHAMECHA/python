print({x: x * x for x in (1, 2, 3, 4)})
print(dict((x, x * x) for x in (1, 2, 3, 4)))
# Out: {1: 1, 2: 4, 3: 9, 4: 16}

print({name: len(name)
       for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6})
print(dict((name, len(name))
           for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6))
# Out: {'Exchange': 8, 'Overflow': 8}

initial_dict = {'x': 1, 'y': 2}
{key: value for key, value in initial_dict.items() if key == 'x'}
# Out: {'x': 1}

my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict)
swapped = {v: k for k, v in my_dict.items()}
print(swapped)
swapped = dict(zip(my_dict.values(), my_dict))
print(swapped)
swapped = dict(zip(my_dict.values(), my_dict.keys()))
print(swapped)
swapped = dict(map(reversed, my_dict.items()))
print(swapped)

# ~ Merging Dictionaries
# * Combine dictionaries and optionally override old values with a nested dictionary comprehension.
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}
print({k: v for d in [dict1, dict2] for k, v in d.items()})
# Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}
