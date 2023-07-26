import math
# * custom module created in same folder
# * Import whole module
import text
# * Particular module
from text import sayHello
# * Aliased
import text as custom_module

# * List out built in functions
print(dir(__builtins__))

# * About functions
print(help(max))

# * Particular module's all functions
print(dir(math))
# * Get documentation of given module
print(math.__doc__)

# * Get doc string of module
print(text.__doc__)
print(custom_module.__doc__)
# * Particular function's doc string
print(sayHello.__doc__)


# ~ If the module is inside a directory and needs to be detected by python, the directory should contain a file named __init__.py.
