
# * Generator expressions are very similar to list comprehensions. The main difference is that it does not create a full set of results at once; it creates a generator object which can then be iterated over.

# list comprehension
[x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# generator comprehension
g = (x**2 for x in range(10))
print(g)
# Output: <generator object <genexpr> at 0x11b4b7c80>

# ! We use xrange since it too creates a generator object. If we would use range, a list would be created. Also, xrange exists only in later version of python 2. In python 3, range just returns a generator. For more information, see the Differences between range and xrange functions example.

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# * Generator expressions are lazily evaluated, which means that they generate and return each value only when the generator is iterated. This is often useful when iterating through large datasets, avoiding the need to create a duplicate of the dataset in memory:

for square in (x**2 for x in range(10)):
    print(square)
