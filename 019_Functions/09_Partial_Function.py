from functools import partial


def raise_power(x, y):
    return x**y

# Let's suppose y can be one of [3,4,5] and let's say you don't want offer end user the possibility to use such function since it is very computationally intensive. In fact you would check if provided y assumes a valid value and rewrite your function as:


def raise_power2(x, y):
    if y in (3, 4, 5):
        return x**y
    raise Exception("You should provide a valid exponent")

# raise_power2(2, 10)

# Messy? Let's use the abstract form and specialize it to all three cases: let's implement them partially


raise_to_three = partial(raise_power, y=3)
raise_to_four = partial(raise_power, y=4)
raise_to_five = partial(raise_power, y=5)

print(raise_to_five(10))
# 100000

# print(raise_to_four(10, 7))
# !TypeError: raise_power() got multiple values for argument 'y'
