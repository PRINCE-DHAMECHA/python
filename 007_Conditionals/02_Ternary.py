
# * The ternary operator is used for inline conditional expressions. It is best used in simple, concise operations that are easily read.

n = 5
print("Greater than 2") if n > 2 else print("Smaller than or equal to 2")

# * The result of this expression will be as it is read in English - if the conditional expression is True, then it will evaluate to the expression on the left side, otherwise, the right side.

# * Ternary operations can also be nested, as here:

n = 5
print("Hello") if n > 10 else print("Goodbye") if n > 5 else print("Good day")
