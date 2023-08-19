
# * This module implements some useful functions on pathnames. The path parameters can be passed as either strings, or bytes. Applications are encouraged to represent file names as (Unicode) character strings.


# * To join two or more path components together, firstly import os module of python and then use following:

import os

print(os.path.join('a', 'b', 'c'))

# * The advantage of using os.path is that it allows code to remain compatible over all operating systems, as this uses the separator appropriate for the platform it's running on.
