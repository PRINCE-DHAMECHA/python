import sys


def cursing(depth):
    try:
        cursing(depth + 1)  # actually, re-cursing
    except RuntimeError as RE:
        print('I recursed {} times!'.format(depth))


cursing(0)
# Out: I recursed 1083 times!

# * It is possible to change the recursion depth limit by using sys.setrecursionlimit(limit) and check this limit by sys.getrecursionlimit().

sys.setrecursionlimit(2000)
cursing(0)
# Out: I recursed 1995 times!

# * One method for creating recursive lambda functions involves assigning the function to a variable and then referencing that variable within the function itself. A common example of this is the recursive calculation of the factorial of a number - such as shown in the following code:

# lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
# print(lambda_factorial(4)) # 4 * 3 * 2 * 1 = 12 * 2 = 24
