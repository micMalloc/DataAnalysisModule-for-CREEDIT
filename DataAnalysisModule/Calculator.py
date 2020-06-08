import pymysql
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from datetime import datetime, timedelta, date
from matplotlib import rc, font_manager


path = '/Library/Fonts/NanumGothicBold.otf'
font_name = font_manager.FontProperties(fname=path, size=15).get_name()
plt.rc('font', family=font_name)

connection = pymysql.connect(host='localhost', user='root', password='gml7594!tn', db='creedit', charset='utf8')

cursor = connection.cursor()

target = datetime.now()
end = date(target.year, target.month, target.day)

target = datetime.now() - timedelta(days=17)
start = date(target.year, target.month, target.day)

sql = "select cid, time_stamp, subscriberCount from stat where time_stamp between \'{0}\' and \'{1}\' order by time_stamp".format(start, end)

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

channels = {}

for cid, date, subscriber in rows:
    channels[cid] = {}

    if date != start:
        break

for cid, date, subscriber in rows:
    if cid == 'UCAXj6Qnek_9qUF5HQEgfYXA':
        continue
    try:
        channels[cid][date] = subscriber
    except KeyError:
        print(cid, date, subscriber)
    # channels[cid][date] = subscriber

delta = end - start
date_list = []

dx = delta.days

target_channel = ""
val = 0

for key in channels.keys():
    dy = channels[key][end] - channels[key][start]
    
    if val <= (dy / dx):
        if val == (dy / dx):
            if channels[target_channel][end] < channels[key][end]:
                target_channel = key
                val = dy / dx
        else:
            target_channel = key
            val = dy / dx

print(target_channel, val, channels[target_channel][end])

dates = []
subs = []

for cid, date, subscriber in rows:
    if cid == target_channel:
        dates.append(str(date))
        subs.append(subscriber)
        print(str(date), subscriber)

cname = ""

sql = "select cname from channels where cid = \'{0}\'".format(target_channel)
print(sql)
cursor.execute(sql)

cname = cursor.fetchall()[0][0]

print(cname)

figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(dates, subs, label=target_channel)
plt.xlabel('날짜')
plt.ylabel('구독자')
plt.title(cname)
plt.show()

sql = "select cid, subscriberCount from stat where time_stamp = \'{0}\'".format(end)

cursor.execute(sql)
_rows = cursor.fetchall()

max_subs = 0
max_cid = ""

for row in _rows:
    cid = row[0]
    subs = row[1]

    if max_subs < subs:
        max_subs = subs
        max_cid = cid

dates = []
subs = []

for cid, date, subscriber in rows:
    if cid == max_cid:
        dates.append(str(date))
        subs.append(subscriber)

sql = "select cname from channels where cid = \'{0}\'".format(max_cid)
print(sql)
cursor.execute(sql)

cname = cursor.fetchall()[0][0]

figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(dates, subs, label=target_channel)
plt.xlabel('날짜')
plt.ylabel('구독자')
plt.title(cname)
plt.show()

# for i in range(delta.days + 1):
#     pass
#     # print(start + timedelta(days=i))