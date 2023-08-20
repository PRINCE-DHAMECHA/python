
# * Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input.below are functional techniques common to many languages: such as lambda, map, reduce.

# ~ Lambda Function

# * An anonymous, inlined function defined with lambda. The parameters of the lambda are defined to the left of the colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly) returned.

# def s(x): return x*x
# s(2)
# =>4

# ~ Map Function

# * Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It returns the new collection.

from functools import reduce
name_lengths = map(len, ["Mary", "Isla", "Sam"])
it = iter(name_lengths)
for num in it:
    print(num)
# => [4, 4, 3]

# ~ Reduce Function

# * Reduce takes a function and a collection of items. It returns a value that is created by combining the items.


total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)
# =>10

# ~  Filter Function

arr = [1, 2, 3, 4, 5, 6]
op = filter(lambda x: x > 4, arr)
for num in op:
    print(num)
# 5
# 6
