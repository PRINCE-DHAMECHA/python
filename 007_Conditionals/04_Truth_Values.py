
# * The following values are considered falsey, in that they evaluate to False when applied to a boolean operator.

# None
# False
# 0, or any numerical value equivalent to zero, for example 0L, 0.0, 0j
# Empty sequences: '', "", (), []
# Empty mappings: {}
# User-defined types where the __bool__ or __len__ methods return 0 or False

# * All other values in Python evaluate to True.

# A common mistake is to simply check for the Falseness of an operation which returns different Falsey values where the difference matters. For example, using if foo() rather than the more explicit if foo() is None
