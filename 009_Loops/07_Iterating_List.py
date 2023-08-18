collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]

for item in collection:
    i1 = item[0]
    i2 = item[1]
    i3 = item[2]
    print(i1, i2, i3)
    # logic

for item in collection:
    i1, i2, i3 = item
    print(i1, i2, i3)
    # logic

for i1, i2, i3 in collection:
    print(i1, i2, i3)
    # logic

# This will also work for most types of iterables, not just tuples

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

# * Suppose you have a long list of elements and you are only interested in every other element of the list. Perhaps you only want to examine the first or last elements, or a specific range of entries in your list. Python has strong indexing built-in capabilities. Here are some examples of how to achieve these scenarios.

for s in lst:
    print(s[:1])  # print the first letter

# * Often you need both the element and the index of that element. The enumerate keyword performs that task.

for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))

# * If we want to iterate over a range (remembering that Python uses zero-based indexing), use the range keyword.

for i in range(2, 4):
    print("lst at %d contains %s" % (i, lst[i]))

# * The list may also be sliced. The following slice notation goes from element at index 1 to the end with a step of 2. The two for loops give the same result.

for s in lst[1::2]:
    print(s)

for i in range(1, len(lst), 2):
    print(lst[i])
