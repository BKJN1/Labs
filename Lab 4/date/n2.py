import datetime as dt

print((dt.datetime.today() - dt.timedelta(days=1)).strftime("%d %b %Y"))
print((dt.datetime.today()).strftime("%d %b %Y"))
print((dt.datetime.today() + dt.timedelta(days=1)).strftime("%d %b %Y"))