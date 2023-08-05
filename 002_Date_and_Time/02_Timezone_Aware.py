
# * By default all datetime objects are naive. To make them timezone-aware, you must attach a tzinfo object, which provides the UTC offset and timezone abbreviation as a function of date and time.

from dateutil import tz
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9), 'JST')

dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
print(dt.timetz())
print(dt.tzname())
print(dt.tzname)


# * <= 2.7

JST = tz.tzoffset('JST', 9 * 3600)
dt = datetime(2015, 1, 1, 12, 0, tzinfo=JST)
print(dt)
print(dt.tzname())
