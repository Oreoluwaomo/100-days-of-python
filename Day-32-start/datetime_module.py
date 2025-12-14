import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2003,month=12,day=23,hour=4)
print(date_of_birth)