
# ~Python operators have a set order of precedence, which determines what operators are evaluated first in a potentially ambiguous expression. For instance, in the expression 3 * 2 + 7, first 3 is multiplied by 2, and then the result is added to 7, yielding 13. The expression is not evaluated the other way around, because * has a higher precedence than +.

# * Python follows PEMDAS rule. PEMDAS stands for Parentheses, Exponents, Multiplication and Division, and Addition and Subtraction.

# * () -> ** -> * / -> + -

a, b, c, d = 2, 3, 5, 7
a ** (b + c)  # parentheses # 256
a * b ** c  # exponent: same as `a * (b ** c)` # 7776
print(a + b * c / d)  # multiplication / division: same as `a + (b * c / d)`
4.142857142857142

# Order of mul or div will not matter within them
print(b*(c/d))
print((b*c)/d)


print(300 / 300 * 200)
print(300 * 200 / 300)

# ~ Wait a minute... Not always :)
print(1e300 / 1e300 * 1e200)
print(1e300 * 1e200 / 1e300)
