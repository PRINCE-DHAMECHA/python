import dateutil.relativedelta
import datetime
from datetime import date, datetime, timedelta
import calendar


now = datetime.now()
then = datetime(2016, 5, 23)  # datetime.datetime(2016, 05, 23, 0, 0, 0)
print(then, now)

delta = now-then
print((delta))
print(delta.days)
print(delta.seconds)


def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)


def get_n_days_before_date(date_format="%d %B %Y", days_before=120):
    date_n_days_ago = datetime.now() - timedelta(days=days_before)
    return date_n_days_ago.strftime(date_format)


print(get_n_days_before_date("%Y-%B-%d", 30))
print(get_n_days_after_date("%Y-%B-%d", 30))


def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1)
    if not m:
        m = 12
    d = min(date.day, calendar.monthrange(y, m)[1])
    return date.replace(day=d)


next_month = monthdelta(date.today(), 1)
print(next_month)

d = datetime.strptime("2013-03-31", "%Y-%m-%d")
# datetime.datetime(2013, 2, 28, 0, 0)
d2 = d - dateutil.relativedelta.relativedelta(months=1)
print(d, d2)
