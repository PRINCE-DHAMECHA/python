
# * Intersection
print({1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}))  # {3, 4, 5}
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})  # {3, 4, 5}

# * Union
print({1, 2, 3, 4, 5}.union({3, 4, 5, 6}))  # {1, 2, 3, 4, 5, 6}
print({1, 2, 3, 4, 5} | {3, 4, 5, 6})  # {1, 2, 3, 4, 5, 6}

# * Difference
print({1, 2, 3, 4}.difference({2, 3, 5}))  # {1, 4}
print({1, 2, 3, 4} - {2, 3, 5})  # {1, 4}

# *Symmetric difference with
print({1, 2, 3, 4}.symmetric_difference({2, 3, 5}))  # {1, 4, 5}
print({1, 2, 3, 4} ^ {2, 3, 5})  # {1, 4, 5}

# * Superset check
print({1, 2, 3}.issuperset({1, 2}))  # True
print({1, 2} >= {1, 2, 3})  # False

# * Subset check
print({1, 2}.issubset({1, 2, 3}))  # True
print({1, 2} <= {1, 2, 3})  # True

# * Disjoint check
# * Sets a and d are disjoint if no element in a is also in d and vice versa.
print({1, 2}.isdisjoint({3, 4}))  # True
print({1, 2}.isdisjoint({1, 4}))  # False
print(len({1, 2} & {3, 1}) == 0)  # False # Less Efficient
print({1, 2} & {3, 1} == set())  # False # Even less Efficient

# ~ Signal element operation

# * Existence check
print(2 in {1, 2, 3})  # True
print(4 in {1, 2, 3})  # False
print(4 not in {1, 2, 3})  # True

# * Add and Remove
s = {1, 2, 3}
print(s.add(4))  # s == {1,2,3,4}
s.discard(3)  # s == {1,2,4}
s.discard(5)  # s == {1,2,4} # No error
s.remove(2)  # s == {1,4}
print(s)
# print(s.remove(2))  # ! KeyError

# * Testing membership
print(1 in {2, 31, 1})
print(1 in {2, 31, 0})

# ~ Set operations return new sets, but have the corresponding in-place versions:

# method -- in-place operation -- in-place method
# union -- s |= t -- update
# intersection -- s &= t -- intersection_update
# difference -- s -= t -- difference_update

s = {1, 2}
s.update({3, 4})
print(s)
