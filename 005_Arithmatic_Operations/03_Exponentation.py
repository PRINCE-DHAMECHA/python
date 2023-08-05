import math
import cmath
import operator
a, b = 2, 3
print(a ** b)
print(pow(a, b))

# * Always float
print(math.pow(a, b))

# * Another difference between the built-in pow and math.pow is that the built-in pow can accept three arguments
print(pow(a, b, 3))  # (a+b)%4

print(operator.pow(a, b))

c = 4
print(math.sqrt(c))
# * complex
print(cmath.sqrt(c))

# ~ To compute other roots, such as a cube root, raise the number to the reciprocal of the degree of the root. This could be done with any of the exponential functions or operator.

x = 8
print(math.pow(x, 1/3))
print(x**(1/3))
# Also float
print(pow(x, 1/3))
# Int
print(pow(x, 3))

# * The function math.exp(x) computes e ** x.

print(math.exp(0))
print(math.exp(1))

# * The function math.expm1(x) computes e ** x - 1. When x is small, this gives significantly better precision than math.exp(x) - 1.

print(math.expm1(0))
print(math.exp(1e-6) - 1)
print(math.expm1(1e-6))
