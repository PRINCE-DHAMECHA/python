# It's possible to compare lists and other sequences lexicographically using comparison operators. Both operands must be of the same type.

[1, 10, 100] < [2, 10, 100]
# True, because 1 < 2
[1, 10, 100] < [1, 10, 100]
# False, because the lists are equal
[1, 10, 100] <= [1, 10, 100]
# True, because the lists are equal
[1, 10, 100] < [1, 10, 101]
# True, because 100 < 101
[1, 10, 100] < [0, 10, 100]
# False, because 0 < 1

# * If one of the lists is contained at the start of the other, the shortest list wins.

[1, 10] < [1, 10, 100]
# True
[1, 9] < [1, 10, 100]
# True
print([1, 9, 99, 11] < [1, 10, 100])
# True
