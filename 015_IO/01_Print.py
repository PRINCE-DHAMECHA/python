
# ^ Python 3.x Version ≥ 3.0
# * In Python 3, print functionality is in the form of a function:
print("This string will be displayed in the output")
# * This string will be displayed in the output
print("You can print \nescape characters too.")
# * You can print escape characters too.

# Python 2.x Version ≥ 2.3
# In Python 2, print was originally a statement, as shown below.
# print "This string will be displayed in the output"
# # This string will be displayed in the output
# print "You can print \n escape characters too."
# # You can print escape characters too.

# * Note: using from __future__ import print_function in Python 2 will allow users to use the print() function the same as Python 3 code. This is only available in Python 2.6 and above.

# * In Python 3.x, the print function has an optional end parameter that is what it prints at the end of the given string. By default it's a newline character, so equivalent to this:

print("Hello, ", end="\n")
print("Mom!")
# Hello,
# Mom!

print("Hello, ", end="")
print("Mom!")
# Hello, Mom!
print("Hello, ", end="<br> ")
print("Mom!")
# Hello, <br> Mom!
print("Hello, ", end="BREAK ")
print("Mom!")
# Hello, BREAK Mom!
