
# ~ In Python you can define a series of conditionals using if for the first one, elif for the rest, up until the final (optional) else for anything not caught by the other conditionals/

number = 5
if number > 2:
    print("Number is bigger than 2.")
elif number < 2:  # Optional clause (you can have multiple elifs)
    print("Number is smaller than 2.")
else:  # Optional clause (you can only have one else)
    print("Number is 2.")
