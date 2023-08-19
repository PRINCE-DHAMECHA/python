tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1', '2', '3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

# ~ Tuple Length
# * The function len returns the total length of the tuple
len(tuple1)
# Out: 5

# ~ Max of a tuple
# * The function max returns item from the tuple with the max value
max(tuple1)
# Out: 'e'
max(tuple2)
# Out: '3'

# ~ Min of a tuple
# * The function min returns the item from the tuple with the min value
min(tuple1)
Out: 'a'
min(tuple2)
Out: '1'

# ~ Convert a list into tuple
# * The built-in function tuple converts a list into a tuple.
list = [1, 2, 3, 4, 5]
tuple(list)
# Out: (1, 2, 3, 4, 5)

# ~ Tuple concatenation
# * Use + to concatenate two tuples
tuple1 + tuple2
# Out: ('a', 'b', 'c', 'd', 'e', '1', '2', '3')

# ~ Reverse

colors = "red", "green", "blue"
rev = colors[::-1]
# rev: ("blue", "green", "red")
colors = rev
print(colors)
# colors: ("blue", "green", "red")

colors = "red", "green", "blue"
rev = tuple(reversed(colors))
# rev: ("blue", "green", "red")
colors = rev
print(colors)
# colors: ("blue", "green", "red")
