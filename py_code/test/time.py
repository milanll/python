
import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

import calendar

calendar = calendar.month(2017, 12)
print(calendar)

print(time.clock())

import datetime

now = datetime.datetime.now()
print(now)