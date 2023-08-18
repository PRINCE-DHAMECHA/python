
# * These operators compare two types of values, they're the less than and greater than operators. For numbers this simply compares the numerical values to see which is larger:

print(12 > 4)
print(1 > 4)

# * For strings they will compare lexicographically, which is similar to alphabetical order but not quite the same.

print("alpha" < "beta")
# True
print("gamma" > "beta")
# True
print("gamma" < "OMEGA")
# False

# * In these comparisons, lowercase letters are considered 'greater than' uppercase, which is why "gamma" < "OMEGA" is false. If they were all uppercase it would return the expected alphabetical ordering result:

print("GAMMA" < "ORDER")
# True
