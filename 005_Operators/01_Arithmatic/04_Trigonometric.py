import math


a, b = 1, 2

print(math.sin(a))  # returns the sine of 'a' in radians
# Out: 0.8414709848078965
print(math.cosh(b))  # returns the inverse hyperbolic cosine of 'b' in radians
# Out: 3.7621956910836314
print(math.atan(math.pi))  # returns the arc tangent of 'pi' in radians
# Out: 1.2626272556789115
# returns the Euclidean norm, same as math.sqrt(a*a + b*b)
print(math.hypot(a, b))
# Out: 2.23606797749979

# ~ Note that math.hypot(x, y) is also the length of the vector (or Euclidean distance) from the origin (0, 0) to the point (x, y).
# * To compute the Euclidean distance between two points (x1, y1) & (x2, y2) you can use math.hypot as follows
print(math.hypot(2-1, 2-1))

math.degrees(a)
# Out: 57.29577951308232
math.radians(57.29577951308232)
# Out: 1.0
