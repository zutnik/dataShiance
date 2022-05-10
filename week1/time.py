import datetime as dt
import time as tm

# dtnow = dt.datetime.fromtimestamp(tm.time())
# print(dtnow.minute, dtnow.month)
# delta = dt.timedelta(100)  # create a timedelta of 100 days
# print(delta)
# print(today - delta)
# print(today)

today = dt.date.today()
dayVera = dt.datetime.fromisoformat('2020-11-24')
print(today - dayVera.date())
