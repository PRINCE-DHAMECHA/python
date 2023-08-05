from datetime import datetime
from dateutil.tz import tzlocal
import iso8601

# yyyy-mm-dd hh-mm-ss.ssssss
d = str(datetime(2016, 7, 22, 9, 25, 59, 555555))
print(d)

print(str(datetime(2016, 7, 22, 9, 25, 59, 0)))

# But these 2 forms need a different format for strptime. Furthermore, strptime' does not support at all parsing minute timezones that have a:in it, thus2016-07-22 09:25:5 +0300can be parsed, but the standard format2016-07-22 09:25:5 +03:00` cannot.

print(iso8601.parse_date('2016-07-22 09:25:59'))
# datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)
print(iso8601.parse_date('2016-07-22 09:25:59+03:00'))
# datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<FixedOffset '+03:00' ...>)
print(iso8601.parse_date('2016-07-22 09:25:59Z'))
# datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)
print(iso8601.parse_date('2016-07-22T09:25:59.000111+03:00'))
# datetime.datetime(2016, 7, 22, 9, 25, 59, 111, tzinfo=<FixedOffset '+03:00' ...>)
print(iso8601.parse_date('2016-07-22T09:25:59', default_timezone=None))
# datetime.datetime(2016, 7, 22, 9, 25, 59)
print(iso8601.parse_date('2016-07-22T09:25:59Z', default_timezone=None))
# datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)

print(datetime.now().isoformat())
print(datetime.now(tzlocal()).isoformat())
print(datetime.now(tzlocal()).replace(microsecond=0).isoformat())
