import pymysql
from datetime import datetime, timedelta, date

creedit = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='', db='db_creedit', charset='utf8')
manager = creedit.cursor()

CATEGORY = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]

END = 'end'
START = 'start'

manager.execute("truncate table statistics")
creedit.commit()

data = {}

for category in CATEGORY:
    data[category] = {}

target = datetime.now()
end = date(target.year, target.month, target.day)

target = datetime.now() - timedelta(days=11)
start = date(target.year, target.month, target.day)

sql = "select categorymap.category_id, stat.cid, stat.time_stamp, stat.viewCount, stat.subscriberCount from categorymap join stat where categorymap.cid = stat.cid and stat.time_stamp between \'{0}\' and \'{1}\' order by stat.time_stamp".format(str(start), str(end))

manager.execute(sql)
rows = manager.fetchall()

for cno, cid, date, views, subs in rows:
    data[cno][cid] = {}
    data[cno][cid][END] = str(end)

channel_id = ""
category = 0

for cno, cid, date, views, subs in rows:
    date = str(date)

    if category != cno:
        category = cno
        data[cno][cid][START] = str(date)

    if subs != 0:
        data[cno][cid][date] = subs
    else:
        data[cno][cid][date] = views

delta = end - start
channels = {}

for cno in CATEGORY:
    dx = delta.days
    target_channel = ""
    val = 0

    for key in data[cno].keys():
        if START not in data[cno][key].keys():
                continue

        u = data[cno][key][START]
        v = data[cno][key][END]

        dy = data[cno][key][v] - data[cno][key][u]

        if target_channel is "":
            target_channel = key
            val = dy / dx
            continue

        if val <= (dy / dx):
            if val == (dy / dx):
                if data[cno][target_channel][v] < data[cno][key][v]:
                    target_channel = key
                    val = dy / dx
            else:
                target_channel = key
                val = dy / dx

    channels[cno] = target_channel

for cno in CATEGORY:
    if channels[cno] == "":
        continue

    sql = "select cname from channels where cid = \'{0}\'".format(channels[cno])
    manager.execute(sql)
    cname = manager.fetchall()[0][0]
    print(cno, cname)

    for row in data[cno][channels[cno]]:
        if row is END:
            continue
        if row is START:
            continue
        print(row, data[cno][channels[cno]][row])
        sql = "insert into statistics(category, time_stamp, subscriberCount, viewCount) values(%s, %s, %s, %s)"
        manager.execute(sql, (cno, row, data[cno][channels[cno]][row], 0))

creedit.commit()
creedit.close()


# import pymysql
# from datetime import datetime, timedelta, date

# creedit = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='ehdgus93!', db='db_creedit', charset='utf8')
# manager = creedit.cursor()

# CATEGORY = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
# ]

# END = 'end'
# START = 'start'

# manager.execute("truncate table statistics")
# creedit.commit()

# data = {}

# for category in CATEGORY:
#     data[category] = {}

# target = datetime.now()
# end = date(target.year, target.month, target.day)

# target = datetime.now() - timedelta(days=11)
# start = date(target.year, target.month, target.day)

# sql = "select categorymap.category_id, stat.cid, stat.time_stamp, stat.viewCount, stat.subscriberCount from categorymap join stat where categorymap.cid = stat.cid and stat.time_stamp between \'{0}\' and \'{1}\' order by stat.time_stamp".format(str(start), str(end))

# manager.execute(sql)
# rows = manager.fetchall()

# for cno, cid, date, views, subs in rows:
#     data[cno][cid] = {}
#     data[cno][cid][END] = str(end)

# channel_id = ""
# category = 0

# for cno, cid, date, views, subs in rows:
#     date = str(date)

#     if category != cno:
#         category = cno
#         data[cno][cid][START] = str(date)

#     if subs != 0:
#         data[cno][cid][date] = subs
#     else:
#         data[cno][cid][date] = views

# for cno in CATEGORY:
#     if channels[cno] == "":
#         continue

#     sql = "select cname from channels where cid = \'{0}\'".format(channels[cno])
#     manager.execute(sql)
#     cname = manager.fetchall()[0][0]
#     print(cno, cname)

#     for row in data[cno][channels[cno]]:
#         if row is END:
#             continue
#         if row is START:
#             continue
#         print(row, data[cno][channels[cno]][row])
#         sql = "insert into statistics(category, time_stamp, subscriberCount, viewCount) values(%s, %s, %s, %s)"
#         manager.execute(sql, (cno, row, data[cno][channels[cno]][row], 0))

# creedit.commit()
# creedit.close()
# import pymysql

# creedit = pymysql.connect(host='203.245.30.13', user='ehdgus93', password='ehdgus93!', db='db_creedit', charset='utf8')
# manager = creedit.cursor()

# conn = pymysql.connect(host='localhost', user='root', password='gml7594!tn', db='creedit', charset='utf8')
# cursor = conn.cursor()

# sql = "select * from stat where time_stamp > \'2020-05-19\'"

# manager.execute(sql)
# rows = manager.fetchall()

# sql = 'insert into stat(cid, time_stamp, viewCount, subscriberCount, commentCount, hiddenSubscriberCount, videoCount) values(%s, %s, %s, %s, %s, %s, %s)'

# for row in rows:
#     cursor.execute(sql, (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# creedit.close()
# conn.commit()
# conn.close()