import datetime as dt

def diff(date1: str, date2: str, format: str = "%Y-%m-%d %H:%M:%S") -> int:
    d1= dt.datetime.strptime(date1, format)
    d2= dt.datetime.strptime(date2, format)
    return abs(int((d1-d2).total_seconds()))
    

date1 = "2020-02-04 12:30:58"
date2 = "2020-03-05 12:20:20"

dif = diff(date1, date2)

print("date 1: '2020-02-04 12:30:58'")
print("date 2: '2020-03-05 12:20:20'")
print(f"difference: {dif} seconds")
