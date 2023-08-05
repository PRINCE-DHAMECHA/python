
# ~ By default, the math.log function calculates the logarithm of a number, base e. You can optionally specify a base as the second argument.

import math
import cmath

math.log(5)  # = 1.6094379124341003
# optional base argument. Default is math.e
math.log(5, math.e)  # = 1.6094379124341003
cmath.log(5)  # = (1.6094379124341003+0j)
math.log(1000, 10)  # 3.0 (always returns float)
cmath.log(1000, 10)  # (3+0j)

# * Special variations of the math.log function exist for different bases.

# Logarithm base e - 1 (higher precision for low values)
math.log1p(5)  # = 1.791759469228055
# Logarithm base 2
math.log2(8)  # = 3.0
# Logarithm base 10
math.log10(100)  # = 2.0
cmath.log10(100)  # = (2+0j)
