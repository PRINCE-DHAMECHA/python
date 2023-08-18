
# * A while loop will cause the loop statements to be executed until the loop condition is falsey. The following code will execute the loop statements a total of 4 times.

import cmath
i = 0
while i < 4:
    # loop statements
    i = i + 1

# * While the above loop can easily be translated into a more elegant for loop, while loops are useful for checking if some condition has been met. The following loop will continue to execute until myObject is ready.

# myObject = anObject()
# while myObject.isNotReady():
#  myObject.tryToGetReady()

# complex_num = cmath.sqrt(-1)
# while complex_num:  # You can also replace complex_num with any number, True or a value of any type
#     print(complex_num)  # Prints 1j forever
