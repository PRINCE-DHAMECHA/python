import datetime

day_delta = datetime.timedelta(days=5)
start_date = datetime.date.today()
end_date = start_date + 10*day_delta


for i in range((end_date-start_date).days):
    print(start_date+i*day_delta)
