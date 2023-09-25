
# * Python supports a translate method on the str type which allows you to specify the translation table (used for replacements) as well as any characters which should be deleted in the process.

# * str.translate(table[, deletechars])

# ~ Parameter - Description

# * table - It is a lookup table that defines the mapping - from one character to another.
# * deletechars A list of characters which are to be removed from the string.

# * The maketrans method (str.maketrans in Python 3 and string.maketrans in Python 2) allows you to generate a translation table.

translation_table = str.maketrans("aeiou", "12345")
my_str = "this is my string Yo-Yo"
new_str = my_str.translate(translation_table)
print(my_str)
print(new_str)
