
# *Python uses indentation to define control and loop constructs. This contributes to Python's readability, however, it requires the programmer to pay close attention to the use of whitespace. Thus, editor miscalibration could result in code that behaves in unexpected ways.

# *Python uses the colon symbol (: ) and indentation for showing where blocks of code begin and end (If you come from another language, do not confuse this with somehow being related to the ternary operator). That is , blocks in Python, such as functions, loops, if clauses and other constructs, have no ending identifiers. All blocks start with a colon and then contain the indented lines below it.

a = 1
b = 2

if a > b:  # ^ If block starts here
    print(a)  # ^ This is part of the if block
else:  # ^ else must be at the same level as if
    print(b)  # ^ This line is part of the else block

# * Can be written in same lines as shown
# if a > b: print(a)
# else: print(b)

# * An empty block causes an IndentationError. Use pass (a command that does nothing) when you have a block with no content:


def will_be_implemented_later():
    pass

# !mixing tabs and spaces in indentation is strongly discouraged
