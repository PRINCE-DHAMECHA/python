
# * A process that is repeated more than one time by applying the same logic is called an Iteration.  In programming languages like python, a loop is created with few conditions to perform iteration till it exceeds the limit. If the loop is executed 6 times continuously, then we could say the particular block has iterated 6 times.

a = [0, 5, 10, 15, 20]
for i in a:
    if i % 2 == 0:
        print(str(i)+' is an Even Number')
    else:
        print(str(i)+' is an Odd Number')


# ~ Iterator
# * An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc. Iterators are implemented using a class and a local variable for iterating is not required here, It follows lazy evaluation where the evaluation of the expression will be on hold and stored in the memory until the item is called specifically which helps us to avoid repeated evaluation. As lazy evaluation is implemented, it requires only 1 memory location to process the value and when we are using a large dataset then, wastage of RAM space will be reduced the need to load the entire dataset at the same time will not be there.

# ~ Using an iterator-

# * iter() keyword is used to create an iterator containing an iterable object.
# * next() keyword is used to call the next element in the iterable object.
# * After the iterable object is completed, to use them again reassign them to the same object.

iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
