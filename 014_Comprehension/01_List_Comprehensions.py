
# ~ List comprehensions in Python are concise, syntactic constructs. They can be utilized to generate lists from other lists by applying functions to each element in the list. The following section explains and demonstrates the use of these expressions

# * A list comprehension creates a new list by applying an expression to each element of an iterable. The most basic form is:

# ^ [ <expression> for <element> in <iterable> if <condition> ]

# * Each <element> in the <iterable> is plugged in to the <expression> if the (optional) <condition> evaluates to true. All results are returned at once in the new list. Generator expressions are evaluated lazily, but list comprehensions evaluate the entire iterator immediately - consuming memory proportional to the iterator's length.

from random import randrange
squares = [x * x for x in (1, 2, 3, 4)]
print(squares)
# squares: [1, 4, 9, 16]
# * The for expression sets x to each value in turn from (1, 2, 3, 4). The result of the expression x * x is appended to an internal list. The internal list is assigned to the variable squares when completed

# * Besides a speed increase (as explained here), a list comprehension is roughly equivalent to the following for-loop:
squares = []
for x in (1, 2, 3, 4):
    squares.append(x * x)
# squares: [1, 4, 9, 16]

# * Get a list of uppercase characters from a string
[s.upper() for s in "Hello World"]
# ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# * Strip off any commas from the end of strings in a list
[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
# ['these', 'words', 'mostly', 'have,commas']

# ~ else
# else can be used in List comprehension constructs, but be careful regarding the syntax. The if/else clauses should be used before for loop, not after:

# * create a list of characters in apple, replacing non vowels with '*'
# Ex - 'apple' --> ['a', '*', '*', '*' ,'e']
# [x for x in 'apple' if x in 'aeiou' else '*'] # ! SyntaxError: invalid syntax

# * When using if/else together use them before the loop
[x if x in 'aeiou' else '*' for x in 'apple']
# ['a', '*', '*', '*', 'e']

[2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]
# Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

# ~ Double Iteration

# * Order of double iteration [... for x in ... for y in ...] is either natural or counter-intuitive. The rule of thumb is to follow an equivalent for loop:

text = (("Hi", "Prince!"), ("What's", "up?"))

print([word for sentence in text for word in sentence])

# ~ In-place Mutation and Other Side Effects

# * Before using list comprehension, understand the difference between functions called for their side effects (mutating, or in-place functions) which usually return None, and functions that return an interesting value.

# * Many functions (especially pure functions) simply take an object and return some object. An in-place function modifies the existing object, which is called a side effect. Other examples include input and output operations such as printing.

# * list.sort() sorts a list in-place (meaning that it modifies the original list) and returns the value None. Therefore, it won't work as expected in a list comprehension:

lst = [[2, 1], [4, 3], [0, 1]]
print([x.sort() for x in lst])
# [None, None, None]
print(lst)
# [[1, 2], [3, 4], [0, 1]]

# ^ Instead, sorted() returns a sorted list rather than sorting in-place:

lst = [[2, 1], [4, 3], [0, 1]]
print([sorted(x) for x in lst])
# [None, None, None]
print(lst)
# [[2, 1], [4, 3], [0, 1]]

# * Using comprehensions for side-effects is possible, such as I/O or in-place functions. Yet a for loop is usually more readable. While this works in Python 3:

[print(x) for x in (1, 2, 3)]

# Instead use:

for x in (1, 2, 3):
    print(x)

# * In some situations, side effect functions are suitable for list comprehension. random.randrange() has the side effect of changing the state of the random number generator, but it also returns an interesting value. Additionally, next() can be called on an iterator

# * The following random value generator is not pure, yet makes sense as the random generator is reset every time the expression is evaluated:

[randrange(1, 7) for _ in range(10)]
# [2, 3, 2, 1, 1, 5, 2, 4, 3, 5]

print(
    [
        x for x
        in 'foo'
        if x not in 'bao'
    ])

# ~ Avoid repetitive and expensive operations using conditional clause


def f(x):
    import time
    time.sleep(.1)  # Simulate expensive function
    return x**2


# [f(x) for x in range(1000) if f(x) > 10][16, 25, 36, ...]

# * This results in two calls to f(x) for 1,000 values of x: one call for generating the value and the other for checking the if condition. If f(x) is a particularly expensive operation, this can have significant performance implications. Worse, if calling f() has side effects, it can have surprising results.

# * Instead, you should evaluate the expensive operation only once for each value of x by generating an intermediate iterable (generator expression) as follows:

# [v for v in (f(x) for x in range(1000)) if v > 10]


data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)
# Out: [1, 2, 3, 4, 5, 6]

data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output)
# Out: [1, 2, 3, 4, 5, 6]

# * the nested comprehension is also significantly faster.

[x + y for x, y in [(1, 2), (3, 4), (5, 6)]]
# Out: [3, 7, 11]
[x + y for x, y in zip([1, 3, 5], [2, 4, 6])]
# Out: [3, 7, 11]

# * Note however, if the expression that begins the comprehension is a tuple then it must be parenthesized:
# [x, y for x, y in [(1, 2), (3, 4), (5, 6)]] # ! SyntaxError: invalid syntax
[(x, y) for x, y in [(1, 2), (3, 4), (5, 6)]]
# Out: [(1, 2), (3, 4), (5, 6)]

print(sum(1 for x in range(1000) if x % 2 == 0 and '9' in str(x)))

# 1. Iterate over the elements in range(1000).
# 2. Concatenate all the needed if conditions.
# 3. Use 1 as expression to return a 1 for each item that meets the conditions.
# 4. Sum up all the 1s to determine number of items that meet the conditions.

# * Quantitative data is often read in as strings that must be converted to numeric types before processing. The types of all list items can be converted with either a List Comprehension or the map() function.

# Convert a list of strings to integers.
items = ["1", "2", "3", "4"]
[int(item) for item in items]
# Out: [1, 2, 3, 4]
# Convert a list of strings to float.
items = ["1", "2", "3", "4"]
map(float, items)
# Out:[1.0, 2.0, 3.0, 4.0]

# ~ Nested List Comprehensions

# List Comprehension with nested loop
[x + y for x in [1, 2, 3] for y in [3, 4, 5]]
# Out: [4, 5, 6, 5, 6, 7, 6, 7, 8]
# Nested List Comprehension
[[x + y for x in [1, 2, 3]] for y in [3, 4, 5]]
# Out: [[4, 5, 6], [5, 6, 7], [6, 7, 8]]

# * The Nested example is equivalent to
l = []
for y in [3, 4, 5]:
    temp = []
    for x in [1, 2, 3]:
        temp.append(x + y)
    l.append(temp)

# * One example where a nested comprehension can be used it to transpose a matrix.
# ! Only square matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
[[row[i] for row in matrix] for i in range(len(matrix))]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['6', '7', '8', '9']
# Two lists
[(i, j) for i, j in zip(list_1, list_2)]
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Three lists
print([(i, j, k) for i, j, k in zip(list_1, list_2, list_3)])
# [(1, 'a', '6'), (2, 'b', '7'), (3, 'c', '8'), (4, 'd', '9')]
