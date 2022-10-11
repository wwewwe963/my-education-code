# การ set Date และชนิดข้อมูลของวันเวลาใน python
import datetime as dt

date1 = dt.datetime.now()

date2 = dt.datetime(
    year=2020, month=2, day=14,
    hour=13, minute=30
)
date3 = dt.datetime(
    year=2020, month=2, day=20,
    hour=16
)
days = dt.timedelta(days=25)

date4 = date2 - days
days2 = date3 - date2
print(date2.strftime('%A %d %B %Y'))


