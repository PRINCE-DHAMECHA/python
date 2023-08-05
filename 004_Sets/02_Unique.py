
# ~ Let's say you've got a list of restaurants -- maybe you read it from a file. You care about the unique restaurants in the list. The best way to get the unique elements from a list is to turn it into a set:

restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
# prints {'Chicken Chicken', "McDonald's", 'Burger King'}

# ! Note that the set is not in the same order as the original list; that is because sets are unordered, just like dicts.

# * This can easily be transformed back into a List with Python's built in list function, giving another list that is the same list as the original but without duplicates:

restaurants = list(set(restaurants))
print(restaurants)
