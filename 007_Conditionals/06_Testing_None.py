
# ~ You'll often want to assign something to an object if it is None, indicating it has not been assigned. We'll use aDate.

# * The simplest way to do this is to use the is None test.

import datetime

aDate = None
if aDate is None:
    aDate = datetime.date.today()
print(aDate)
# ^ (Note that it is more Pythonic to say is None instead of == None.)

# * But this can be optimized slightly by exploiting the notion that not None will evaluate to True in a boolean expression. The following code is equivalent:

aDate = None
if not aDate:
    aDate = datetime.date.today()
print(aDate)

# * But there is a more Pythonic way. The following code is also equivalent:
aDate = None
aDate = aDate or datetime.date.today()
print(aDate)
