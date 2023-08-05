from datetime import datetime
datetime_for_string = datetime(2016, 10, 1, 0, 0)
datetime_string_format = '%b %d %Y, %H:%M:%S'
print(datetime.strftime(datetime_for_string, datetime_string_format))

datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
print(datetime.strptime(datetime_string, datetime_string_format))
# datetime.datetime(2016, 10, 1, 0, 0)
