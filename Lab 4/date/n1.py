import datetime as dt

x = dt.datetime.today() - dt.timedelta(days=5)
print((dt.datetime.today()).strftime("%d %b %Y"))
print(x.strftime("%d %b %Y"))