
# * For zones with daylight savings time, python standard libraries do not provide a standard class, so it is necessary to use a third party library. pytz and dateutil are popular libraries providing time zone classes

import pytz

from datetime import datetime, timedelta
from dateutil import tz
local = tz.gettz()  # Local time
PT = tz.gettz('US/Pacific')  # Pacific time
dt_l = datetime(2015, 1, 1, 12, tzinfo=local)  # I am in EST
dt_pst = datetime(2015, 1, 1, 12, tzinfo=PT)
dt_pdt = datetime(2015, 7, 1, 12, tzinfo=PT)  # DST is handled automatically
print(dt_l)
# 2015-01-01 12:00:00-05:00
print(dt_pst)
# 2015-01-01 12:00:00-08:00
print(dt_pdt)
# 2015-07-01 12:00:00-07:00

# * All edge cases are handled properly when using pytz, but pytz time zones should not be directly attached to time zones through the constructor. Instead, a pytz time zone should be attached using the time zone's localize method:

PT = pytz.timezone('US/Pacific')
dt_pst = PT.localize(datetime(2015, 1, 1, 12))

# * Daylight Time, often referred to as Daylight Saving Time (DST), is a practice observed in many regions around the world where the local time is adjusted forward by one hour during a certain period of the year, typically in the warmer months. The main purpose of Daylight Time is to make better use of natural daylight during the longer days of summer, thereby reducing the need for artificial lighting and potentially conserving energy.
dt_pdt = PT.localize(datetime(2015, 11, 1, 0, 30))
print(dt_pst)
# 2015-01-01 12:00:00-08:00
print(dt_pdt)
# 2015-11-01 00:30:00-07:00
