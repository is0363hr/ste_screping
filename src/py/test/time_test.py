import datetime

now = datetime.datetime.now() - datetime.timedelta(minutes=50)
time = list(now.strftime("%Y%m%d%H%M"))
print(time)
time = list(datetime.datetime.now().strftime("%Y%m%d%H%M"))
print(time)