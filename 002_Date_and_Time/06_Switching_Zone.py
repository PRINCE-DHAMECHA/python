from datetime import datetime
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

utc_now = datetime.utcnow()
print(utc_now)  # Not timezone-aware.
utc_now = utc_now.replace(tzinfo=utc)
print(utc_now)  # Timezone-aware.
local_now = utc_now.astimezone(local)
print(local_now)  # Converted to local time.
