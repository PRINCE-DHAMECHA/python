
# ~ append()

import array

my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.append(6)
print(my_array)

# ~ insert()

# * We can use the insert() method to insert a value at any index of the array. Here is an example
my_array.insert(2, 5)
print(my_array)

# * A python array can be extended with more than one value using extend() method. Here is an example

# ~ extend()

my_array = array.array('i', [1, 2, 3, 4, 5])
my_extnd_array = array.array('i', [7, 8, 9, 10])
my_array.extend(my_extnd_array)
print(my_extnd_array)
print(my_array)
# array('i', [1, 2, 3, 4, 5, 7, 8, 9, 10])


# ~ fromlist()

my_array = array.array('i', [1, 2, 3, 4, 5])
c = [11, 12, 13]
my_array.fromlist(c)
print(my_array)

# ~ pop()

my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.pop()
# array('i', [1, 2, 3, 4])

# ~ index()

my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array.index(5))
# 5
my_array = array.array('i', [1, 2, 3, 2, 5])
print(my_array.index(3))
# 3
my_array = array.array('i', [1, 2, 3, 2, 5])
print(my_array.index(1))
# 3


# ~ reverse()

my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.reverse()
# array('i', [5, 4, 3, 2, 1])

# ~ buffer_info()

# This method provides you the array buffer start address in memory and number of elements in array. Here is an example:

my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array.buffer_info())

# ~ count()

# * count() will return the number of times and element appears in an array.

my_array = array.array('i', [1, 2, 3, 3, 5])
my_array.count(3)
# 2

# ~ tolist()

my_array = array.array('i', [1, 2, 3, 4, 5])
c = my_array.tolist()
print(c)
# [1, 2, 3, 4, 5]
