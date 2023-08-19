
import copy
a = [1, 2, 3, 4, 5]

# ~ append()

# Append values 6, 7, and 7 to the list
a.append(6)
a.append(7)
a.append(7)
# a: [1, 2, 3, 4, 5, 6, 7, 7]
# Append another list
b = [8, 9]
a.append(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9]]
# Append an element of a different type, as list elements do not need to have the same type
my_string = "hello world"
a.append(my_string)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9], "hello world"]

# ~ extend(enumerable)
# *  extends the list by appending elements from another enumerable.

a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9, 10]
# Extend list by appending all elements from b
a.extend(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# Extend list with elements from a non-list enumerable:
a.extend(range(3))
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 0, 1, 2]

# * Lists can also be concatenated with the + operator. Note that this does not modify any of the original lists:

a = [1, 2, 3, 4, 5, 6] + [7, 7] + b
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

# ~ index(value, [startIndex])
# * gets the index of the first occurrence of the input value. If the input value is not in the list a ValueError exception is raised. If a second argument is provided, the search is started at that specified index.

a.index(7)
# Returns: 6

# a.index(49)  # ! ValueError, because 49 is not in a.

print(a)
a.index(7, 5)
# Returns: 7

# a.index(7, 8)  # ! ValueError, because there is no 7 starting at index 8

# ~ insert(index, value)
# * inserts value just before the specified index. Thus after the insertion the new element occupies position index.

a.insert(0, 0)  # insert 0 at position 0
a.insert(2, 5)  # insert 5 at position 2
# a: [0, 1, 5, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
print(a)

# ~ pop([index])
# * removes and returns the item at index. With no argument it removes and returns the last element of the list

print(a)
print(a.pop(2))
print(a)
# Returns: 5
# a: [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
a.pop(8)
# Returns: 7
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * With no argument:
a.pop()
# Returns: 10
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ~ remove(value)
# *  removes the first occurrence of the specified value. If the provided value cannot be found, a ValueError is raised
print(a)
a.remove(0)
a.remove(9)
print(a)
# a: [1, 2, 3, 4, 5, 6, 7, 8]
# a.remove(10)  # ! ValueError, because 10 is not in a

# ~ reverse()
# * reverses the list in-place and returns None.
print(a.reverse())  # None
print(a)

# ~ count(value)

a.count(7)
# Returns: 2

# ~ clear()

a.clear()
print(a)

# ~ Replication

# * multiplying an existing list by an integer will produce a larger list consisting of that many copies of the original. This can be useful for example for list initialization:

b = ["blah"] * 3
print(b)
# ['blah', 'blah', 'blah']

b = [1, 3, 5] * 5
# [1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5]

# * Take care doing this if your list contains references to objects (eg a list of lists).

# ~ del

a = list(range(10))
del a[::2]
print(a)
# a = [1, 3, 5, 7, 9]
del a[-1]
print(a)
# a = [1, 3, 5, 7]
del a[:]
print(a)
# a = []

# ~ Copying

# * The default assignment "=" assigns a reference of the original list to the new name. That is, the original name and new name are both pointing to the same list object. Changes made through any of them will be reflected in another. This is often not what you intended.

a = [1, 2, 3, 4, 5]

b = a
a.append(6)
print(a, b, a == b)  # True

# *You can slice it:
b = a[:]
print(a == b)  # True
b.append(6)
print(a == b)  # False

# * You can use the built in list() function:
b = list(a)
print(a == b)  # True
b.append(6)
print(a == b)  # False

# * You can use generic copy.copy():

b = copy.copy(a)
print(a == b)  # True
b.append(6)
print(a == b)  # False

# * If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

# new_list = copy.deepcopy(old_list) #inserts copies of the objects found in the original.

# * The emptiness of a list is associated to the boolean False, so you don't have to check len(lst) == 0, but just lst or not lst

lst = []
if not lst:
    print("list is empty")
# Output: list is empty

# ~ len()

print(len(lst))

# * Note that len() is a built-in function, not a method of a list object.
