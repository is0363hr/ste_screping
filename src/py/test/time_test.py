from datetime import datetime, timedelta

now = datetime.now()
h = sum([int(s) for s in str(now.strftime("%H"))])
m = int(now.strftime("%M")[-1])
tem_time = datetime.now() - timedelta(minutes=m % 5)
time = list(tem_time.strftime("%Y%m%d%H%M"))
if h < 10:
    time[-4:-2] = "0" + str(h)
else:
    time[-4:-2] = str(h)
time = "".join(time)
