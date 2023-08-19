
# ~ If you use a dictionary as an iterator (e.g. in a for statement), it traverses the keys of the dictionary. For example:

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])
# c 3
# b 2
# a 1

print([key for key in d])

for key, value in d.items():
    print(key, value)
