
# * You can compare multiple items with multiple comparison operators with chain comparison. For example

x = 1
y = 2
z = 3

print(x > y > z)
# is just a short form of:
x > y and y > z

print(x < y < z)
print(x < z < y)

p = 5
print(x < y < z < p)

# * The general form is
# a OP b OP c OP d ...

print(1 > -1 < 2 > 0.5 < 100 != 100)
print(1 > -1 < 2 > 0.5 < 100 != 24)

# * As soon as one comparison returns False, the expression evaluates immediately to False, skipping all remaining comparisons.

x > y and print('Hello')
x < y and print('Hello')
