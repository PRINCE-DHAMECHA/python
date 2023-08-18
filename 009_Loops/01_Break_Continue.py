
# ~ When a break statement executes inside a loop, control flow "breaks" out of the loop immediately:

i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

# * The loop conditional will not be evaluated after the break statement is executed. Note that break statements are only allowed inside loops, syntactically. A break statement inside a function cannot be used to terminate loops that called that function.

# ~ A continue statement will skip to the next iteration of the loop bypassing the rest of the current block but continuing the loop. As with break, continue can only appear inside loops:

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

# * break and continue only operate on a single level of loop

# * Python doesn't have the ability to break out of multiple levels of loop at once -- if this behavior is desired, refactoring one or more loops into a function and replacing break with return may be the way to go.

# * If you have a loop inside a function, using return from inside that loop is equivalent to having a break as the rest of the code of the loop is not executed (note that any code after the loop is not executed either)
