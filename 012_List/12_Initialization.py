
# * For immutable elements (e.g. None, string literals etc.):
my_list = [None] * 10
print(my_list)
my_list = ['test'] * 10
print(my_list)

# * For mutable elements, the same construct will result in all elements of the list referring to the same object, for example, for a set:
my_list = [{1}] * 10
print(my_list)
my_list[1].add(2)
print(my_list)

# st = {2}
# st2 = st
# st = {3}
# print(st, st2)  # {3} {2}
# st2 = st
# st.add(2)
# print(st, st2)  # {2, 3} {2, 3}

# st = {2}
# st2 = {2}
# st2.add(3)
# print(st, st2)  # {2} {2, 3}

# Instead, to initialize the list with a fixed number of different mutable objects, use:

my_list = [{1} for _ in range(10)]
print(my_list)
my_list[2].add(2)
print(my_list)  # Will not add in all
