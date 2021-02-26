import datetime as dt

date_now = dt.datetime.now().date()
tmp = [date_now - dt.timedelta(days = i) for i in range (7)]
print(tmp)