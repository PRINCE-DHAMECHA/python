a, b, c, d, e = 3, 2, 2.0, -3, 10

# ~ In Python 3 the / operator performs 'true' division regardless of types. The // operator performs floor division and maintains type.

# * 1 for python<=2.7 and 1.5 for python<=3
print(a/b)

print(a/c)
print(d/b)
print(b/a)
print(d/e)

print(a//b)  # 1
print(a//c)  # 1.0

# int and int (gives an int in Python 2 and a float in Python 3)
# int and float (gives a float)
# int and complex (gives a complex)
# float and float (gives a float)
# float and complex (gives a complex)
# complex and complex (gives a complex)
