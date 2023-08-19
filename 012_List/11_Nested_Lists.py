
# * A good way to visualize a 2d array is as a list of lists. Something like this:
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# * here the outer list lst has three things in it. each of those things is another list: The first one is: [1,2,3], the second one is: [4,5,6] and the third one is: [7,8,9]. You can access these lists the same way you would access another other element of a list, like this:

print(lst[0])
# output: [1, 2, 3]
print(lst[1])
# output: [4, 5, 6]
print(lst[2])
# output: [7, 8, 9]

# * You can then access the different elements in each of those lists the same way:

print(lst[0][0])
# output: 1
print(lst[0][1])
# output: 2

lst[0] = 2

print(lst)

# * Lists in lists in lists in..

lst = [[[111, 112, 113], [121, 122, 123], [131, 132, 133]],
       [[211, 212, 213], [221, 222, 223], [231, 232, 233]],
       [[311, 312, 313], [321, 322, 323], [331, 332, 333]]]

print(lst)

# * Starting with a three-dimensional list:
alist = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]

# * Accessing items in the list:
print(alist[0][0][1])
# 2
# * Accesses second element in the first list in the first list

print(alist[1][1][2])
# 10
# * Accesses the third element in the second list in the second list

# ~ Performing support operations:

alist[0][0].append(11)
print(alist[0][0][2])
# 11
# * Appends 11 to the end of the first list in the first list

# * Using nested for loops to print the list:
for row in alist:  # One way to loop through nested lists
    for col in row:
        print(col)
# [1, 2, 11]
# [3, 4]
# [5, 6, 7]
# [8, 9, 10]
# [12, 13, 14]

# * Note that this operation can be used in a list comprehension or even as a generator to produce efficiencies, e.g.:
print([col for row in alist for col in row])
# [[1, 2, 11], [3, 4], [5, 6, 7], [8, 9, 10], [12, 13, 14]]

# * Not all items in the outer lists have to be lists themselves:
alist[1].insert(2, 15)

# * Inserts 15 into the third position in the second list

# * Another way to use nested for loops. The other way is better but I've needed to use this on occasion:
for row in range(len(alist)):  # A less Pythonic way to loop through lists
    for col in range(len(alist[row])):
        print(alist[row][col])
# [1, 2, 11]
# [3, 4]
# [5, 6, 7]
# [8, 9, 10]
# 15
# [12, 13, 14]

# * Another way to use nested for loops. The other way is better but I've needed to use this on occasion:
for row in range(len(alist)):  # A less Pythonic way to loop through lists
    for col in range(len(alist[row])):
        print(alist[row][col])
# [1, 2, 11]
# [3, 4]
# [5, 6, 7]
# [8, 9, 10]
# 15
# [12, 13, 14]
