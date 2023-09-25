
# ~ Python's string type provides many functions that act on the capitalization of a string. These include:

# * With unicode strings (the default in Python 3), these operations are not 1:1 mappings or reversible. Most of these operations are intended for display purposes, rather than normalization.

# ~ str.casefold()

# * str.casefold creates a lowercase string that is suitable for case insensitive comparisons. This is more aggressivethan str.lower and may modify strings that are already in lowercase or cause string sto grow in length, and is not intended for display purposes.

print("XßΣ".casefold())
# 'xssσ'
print("XßΣ".lower())
# 'xßς'

# ~ str.upper()

# * str.upper takes every character in a string and converts it to its uppercase equivalent, for example:

print("This is a 'string'.".upper())
# "THIS IS A 'STRING'."

# ~ str.lower()

# * str.lower does the opposite; it takes every character in a string and converts it to its lowercase equivalent:

print("This IS a 'string'.".lower())
# "this is a 'string'."

# ~ str.capitalize()

# * str.capitalize returns a capitalized version of the string, that is, it makes the first character have upper case and the rest lower:

print("this Is A 'String'.".capitalize())
# "This is a 'string'."

# ~ str.title()

# * str.title returns the title cased version of the string, that is, every letter in the beginning of a word is made upper case and all others are made lower case:

print("this Is a 'string'".title())
# "This Is A 'String

# ~ str.swapcase()

# * str.swapcase returns a new string object in which all lower case characters are swapped to upper case and all upper case characters to lower:

print("this iS A STRiNG".swapcase())  # Swaps case of each character
# "THIS Is a strIng

# ~ Usage as str class methods

# * It is worth noting that these methods may be called either on string objects (as shown above) or as a class method of the str class (with an explicit call to str.upper, etc.)

print(str.upper("This is a 'string'"))
# "THIS IS A 'STRING'"

# * This is most useful when applying one of these methods to many strings at once in say, a map function.

for i in map(str.upper, ["These", "are", "some", "'strings'"]):
    print(i)
# ['THESE', 'ARE', 'SOME', "'STRINGS'"]
