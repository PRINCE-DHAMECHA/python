
# *Python uses indentation to define control and loop constructs. This contributes to Python's readability, however, it requires the programmer to pay close attention to the use of whitespace. Thus, editor misscalibration could result in code that behaves in unexpected ways.

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

# ? How Indentation is Parsed

# * Whitespace is handled by the lexical analyzer before being parsed.

# * Whitespace is handled by the lexical analyzer before being parsed. The lexical analyzer uses a stack to store indentation levels. At the beginning, the stack contains just the value 0, which is the leftmost position. Whenever a nested block begins, the new indentation level is pushed on the stack, and an "INDENT" token is inserted into the token stream which is passed to the parser. There can never be more than one "INDENT" token in a row (IndentationError).

# * When a line is encountered with a smaller indentation level, values are popped from the stack until a value is on top which is equal to the new indentation level (if none is found, a syntax error occurs). For each value popped, a "DEDENT" token is generated. Obviously, there can be multiple "DEDENT" tokens in a row.

# *  The lexical analyzer skips empty lines (those containing only whitespace and possibly comments), and will never generate either "INDENT" or "DEDENT" tokens for them.

# * At the end of the source code, "DEDENT" tokens are generated for each indentation level left on the stack, until just the 0 is left.


# if foo:
#     if bar:
#         x = 42
# else:
#     print("foo")

# <if> <foo> <:>                    [0]
# <INDENT> <if> <bar> <:>           [0, 4]
# <INDENT> <x> <=> <42>             [0, 4, 8]
# <DEDENT> <DEDENT> <else> <:>      [0]
# <INDENT> <print> <foo>            [0, 2]
# <DEDENT>

# * The parser than handles the "INDENT" and "DEDENT" tokens as block delimiters.

# ! The spacing should be even and uniform throughout. Improper indentation can cause an IndentationError or cause the program to do something unexpected.


def isEven(a):
    if a % 2 == 0:
        return True
        # this next line should be even with the if
        return False


print(isEven(7))  # ! None
