
# ~ When you use or, it will either return the first value in the expression if it's true, else it will blindly return the second value. I.e. or is equivalent to:

def or_(a, b):
    if a:
        return a
    else:
        return b


# ~ OR

x = True
y = True
z = x or y  # z = True
x = True
y = False
z = x or y  # z = True
x = False
y = True
z = x or y  # z = True
x = False
y = False
z = x or y  # z = False


print(2 or 7)  # 2
print(9 or 7)  # 2
# ~ Same logic as per and but or returns second if first is false and first otherwise
