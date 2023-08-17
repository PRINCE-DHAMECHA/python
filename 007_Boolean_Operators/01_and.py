
# ~ For and, it will return its first value if it's false, else it returns the last value:


def and_(a, b):
    if not a:
        return a
    else:
        return b

# ~ In Python you can compare a single element using two binary operators--one on either side:


x = 3.1411111
if 3.14 < x < 3.142:
    print("x is near pi")

# * In many (most?) programming languages, this would be evaluated in a way contrary to regular math: (3.14 < x) < 3.142, but in Python it is treated like 3.14 < x and x < 3.142, just like most non-programmers would expect.

# ~ AND

x = True
y = True
z = x and y  # z = True
x = True
y = False
z = x and y  # z = False
x = False
y = True
z = x and y  # z = False
x = False
y = False
z = x and y  # z = False

print((2 and 5))  # 2 is truthy value so it returns 2 blindly as stated earlier
print((2 and -5))
