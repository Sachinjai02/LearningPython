import datetime

mytime = datetime.time(2, 20)
print(mytime.minute)
print(mytime.hour)
print(mytime)

mytime = datetime.time(2,30,20,345)
print(mytime)
print(type(mytime))

today = datetime.date.today()
print(f" {today} has year {today.year}, month {today.month} and day {today.day}")
print(f"Today in ctime is {today.ctime()}")

my_date = datetime.datetime(2021, 10,3, 14, 20, 1)
print(my_date)

my_date = my_date.replace(year = 2024)
print(my_date)


## Arithmetic on date, datetime objects
date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2020, 11, 3)

result = date1 - date2
print(result)

datetime1 = datetime.datetime(2021, 11, 3, 23, 22)
datetime2 = datetime.datetime(2019, 1, 23, 2)
result = datetime1 - datetime2
print(result)
print(result.seconds)
print(result.total_seconds())