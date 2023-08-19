
# ~ One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot add or modify items once the tuple is initialized. For example:

# * Similarly, tuples don't have .append and .extend methods as list does. Using += is possible, but it changes the binding of the variable, and not the tuple itself:

t1 = (1, 2)
t2 = (3, 2)
t1 += t2
print(t1)

# * Be careful when placing mutable objects, such as lists, inside tuples. This may lead to very confusing outcomes when changing them. For example:

t = (1, 2, 3, [1, 2, 3])
# t[3] += [4, 5] #! TypeError: 'tuple' object does not support item assignment
print(t)

# * You can use the += operator to "append" to a tuple - this works by creating a new tuple with the new element you "appended" and assign it to its current variable; the old tuple is not changed, but replaced!
