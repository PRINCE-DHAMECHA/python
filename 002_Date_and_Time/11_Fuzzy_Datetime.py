from dateutil.parser import parse

print(parse("Today is January 1,2047 at 8:21:00AM", fuzzy=True))
print(parse("Today is January 1,2047 at 8:21:00PM", fuzzy=True))
