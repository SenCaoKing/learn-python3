from datetime import datetime, timedelta, timezone

# 获取当前datetime：
now = datetime.now()
print('now =', now) # now = 2019-05-07 15:13:37.281852
print('type(now) =', type(now)) # type(now) = <class 'datetime.datetime'>

# 用指定日期时间创建datetime：
dt = datetime(2019, 5, 7, 14, 56)
print('dt =', dt) # dt = 2019-05-07 14:56:00

# 把datetime转换为timestamp：
print('datetime -> timestamp:', dt.timestamp()) # datetime -> timestamp: 1557212160.0

# 把timestamp转换为datetime：
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t)) # timestamp -> datetime: 2019-05-07 14:56:00
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t)) # timestamp -> datetime as UTC+0: 2019-05-07 06:56:00

# 从str读取datetime：
cday = datetime.strptime('2019-5-7 15:01:30', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday) # strptime: 2019-05-07 15:01:30

# 把datetime格式化输出：
print('strftime:', cday.strftime('%a, %b %d %H %M')) # strftime: Tue, May 07 15 01

# 对日期进行加减：
print('current datetime =', cday) # current datetime = 2019-05-07 15:01:30
print('current + 10 hours =', cday + timedelta(hours=10)) # current + 10 hours = 2019-05-08 01:01:30
print('current - 1 day =', cday - timedelta(days=1)) # current - 1 day = 2019-05-06 15:01:30
print('current + 2.5 days =', cday + timedelta(days=2, hours=12)) # current + 2.5 days = 2019-05-10 03:01:30

# 把时间从UTC+0时区转换为UTC+8：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt) # UTC+0:00 now = 2019-05-07 07:13:37.300795+00:00
print('UTC+8:00 now =', utc8_dt) # UTC+8:00 now = 2019-05-07 15:13:37.300795+08:00
