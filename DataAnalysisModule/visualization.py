import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pymysql
from matplotlib import rc, font_manager

path = '/Library/Fonts/NanumGothicBold.otf'
font_name = font_manager.FontProperties(fname=path, size=15).get_name()
plt.rc('font', family=font_name)

# LingWai SC
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='creedit',
    charset='utf8'
)

cursor = connection.cursor()

sql = 'select channels.cname, stat.time_stamp, stat.viewCount, stat.subscriberCount from channels join stat on channels.cid = stat.cid'

cursor.execute(sql)

data = cursor.fetchall()

channel = data[0][0]

dates = []
subs = []

for cname, date, view, subscriber in data:
    if channel == cname:
        dates.append(str(date))
        subs.append(subscriber)
    else:
        figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(dates, subs, label=channel)
        plt.xlabel('날짜')
        plt.ylabel('구독자')

        plt.title(channel)
        plt.show()
        
        dates = []
        subs = []
        channel = cname

# plt.plot(dates, subs, label=channel)
# plt.xlabel('date')
# plt.ylabel('subscribers')

figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(dates, subs, label=channel)
plt.xlabel('날짜')
plt.ylabel('구독자')

plt.title(channel)
plt.show()

# plt.legend()
# plt.title('전체')
# figure(num=None, figsize=(10, 9), dpi=80, facecolor='w', edgecolor='k')
# plt.show()