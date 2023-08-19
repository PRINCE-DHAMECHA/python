
# * One common pitfall when using dictionaries is to access a non-existent key. This typically results in a KeyError exception

mydict = {}
# mydict['not there'] #! Error

# * One way to avoid key errors is to use the dict.get method, which allows you to specify a default value to return in the case of an absent key
# value = mydict.get(key, default_value)
value = mydict.get("key", "val")
print(value)

mydict = {}
print(mydict)
# {}
print(mydict.get("foo", "bar"))
# bar

# *Which returns mydict['foo'] if it exists, but otherwise returns 'bar'. Note that this doesn't add key to mydict. So if you want to retain that key value pair, you should use mydict.setdefault(key, default_value), which does store the key value pair.

print(mydict)
# {}
print(mydict.setdefault("foo", "bar"))
# bar
print(mydict.get("foo1", "bar2"))
print(mydict)
# {'foo': 'bar'}

# * An alternative way to deal with the problem is catching the exception

try:
    value = mydict['key']
except KeyError:
    value = 'default_value'
print(value)

# * You could also check if the key is in the dictionary.
if 'key' in mydict:
    value = mydict['key']
else:
    value = 'default_value'


# * Do note, however, that in multi-threaded environments it is possible for the key to be removed from the dictionary after you check, creating a race condition where the exception can still be thrown
