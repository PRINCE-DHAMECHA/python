
# ~ for loops iterate over a collection of items, such as list or dict, and run a block of code with each element from the collection.

for i in [0, 1, 2, 3, 4]:
    print(i)

# * Each iteration sets the value of i to the next element of the list. So first it will be 0, then 1, then 2, etc.

# * range is a function that returns a series of numbers under an iterable form, thus it can be used in for loops:

for i in range(5):
    print(i)

# * for loop can iterate on any iterable object which is an object which defines a __getitem__ or a __iter__ function. The __iter__ function returns an iterator, which is an object with a next function that is used to access the next element of the iterable

for x in range(1, 6):
    print(x)

for x in ['one', 'two', 'three', 'four']:
    print(x)

# * The result will be a special range sequence type in python >=3 and a list in python <=2. Both can be looped through using the for loop.

# * If you want to loop though both the elements of a list and have an index for the elements as well, you can use Python's enumerate function:

for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, ':', item)

# * enumerate will generate tuples, which are unpacked into index (an integer) and item (the actual value from the list). The above loop will print
