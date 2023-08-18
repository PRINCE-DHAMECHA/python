
# * The for and while compound statements (loops) can optionally have an else clause (in practice, this usage is fairly rare).

# * The else clause only executes after a for loop terminates by iterating to completion, or after a while loop terminates by its conditional expression becoming false.

for i in range(3):
    print(i)
else:
    print('done')
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')

# * The else clause does not execute if the loop terminates some other way (through a break statement or by raising an exception):

for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')


# * A for loop with an else clause can be understood the same way. Conceptually, there is a loop condition that remains True as long as the iterable object or sequence still has some remaining elements.

# * The main use case for the for...else construct is a concise implementation of search as for instance:

a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")
