import datetime

diff = datetime.timedelta(days = 145, hours = 10, minutes = 3)
d = datetime.datetime(2010, 3, 2, 12, 15, 0)
d2 = d + diff
print(d2)