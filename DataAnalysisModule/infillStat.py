import pymysql
from datetime import datetime, timedelta, date


local = pymysql.connect(host='localhost', user='root', password='', db='creedit', charset='utf8')
creedit = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='', db='db_creedit', charset='utf8')

cursor = local.cursor()
manager = creedit.cursor()

target = datetime.now()
end = date(target.year, target.month, target.day)

target = datetime.now() - timedelta(days=2)
start = date(target.year, target.month, target.day)

target = datetime.now() - timedelta(days=1)
target = date(target.year, target.month, target.day)

sql = "select * from stat where time_stamp between \'{0}\' and \'{1}\'".format(str(start), str(end))

manager.execute(sql)
rows = manager.fetchall()

data = []

print(target)

mid = int(len(rows) / 2)

for idx in range(0, mid):
    row = []
    
    for i in range(1, len(rows[idx])):
        row.append(rows[idx][i])
    
    data.append(row)

for idx in range(mid, len(rows)):
    # print(data[idx - mid])
    for i in range(1, len(rows[idx])):
        if i == 2:
            data[idx - mid][i - 1] = target
        if i >= 3:
            data[idx - mid][i - 1] += rows[idx][i]
            data[idx - mid][i - 1] /= 2
            data[idx - mid][i - 1] = int(data[idx - mid][i - 1])
        
        if i == 6:
            data[idx - mid][i - 1] = rows[idx][i]
    
    # print(data[idx - mid])

sql = 'insert into stat(cid, time_stamp, viewCount, subscriberCount, commentCount, hiddenSubscriberCount, videoCount) values(%s, %s, %s, %s, %s, %s, %s)'

for idx in range(0, mid):
    cursor.execute(sql, (data[idx][0], data[idx][1], data[idx][2], data[idx][3], data[idx][4], data[idx][5], data[idx][6]))
    manager.execute(sql, (data[idx][0], data[idx][1], data[idx][2], data[idx][3], data[idx][4], data[idx][5], data[idx][6]))
    

local.commit()
local.close()
creedit.commit()
creedit.close()