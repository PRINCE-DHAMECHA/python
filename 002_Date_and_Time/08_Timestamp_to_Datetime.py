import time
from datetime import datetime
seconds_since_epoch = time.time()  # 1469182681.709
# datetime.datetime(2016, 7, 22, 10, 18, 1, 709000)
utc_date = datetime.utcfromtimestamp(seconds_since_epoch)
print(utc_date)
