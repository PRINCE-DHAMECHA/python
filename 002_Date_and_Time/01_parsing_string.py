
# ~ Python >= 3.2

import datetime
# * pip install python-parser
import dateutil.parser

dt = datetime.datetime.strptime(
    "2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

# ~ For other version

dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")
print(dt)
